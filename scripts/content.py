"""Local render CLI. Content is editable data; every write stays under out/."""
from pathlib import Path
from array import array
import argparse, hashlib, json, math, os, re, shutil, subprocess, sys, wave
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / 'public/fonts'


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def write_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def font(size, bold=False):
    return ImageFont.truetype(str(FONTS / ('VeraBd.ttf' if bold else 'Vera.ttf')), size)


def wrap(text, size, width, bold=False):
    """Measured wrapping, with explicit overflow instead of unreadable shrinking."""
    face = font(size, bold)
    lines = []
    for paragraph in str(text).split('\n'):
        line = ''
        for word in paragraph.split():
            if face.getlength(word) > width:
                raise ValueError('A word exceeds the text box; shorten the copy')
            candidate = (line + ' ' + word).strip()
            if face.getlength(candidate) > width:
                lines.append(line)
                line = word
            else:
                line = candidate
        lines.append(line)
    return lines


def text_block(draw, text, x, y, width, size, color, bold=False, max_lines=None):
    lines = wrap(text, size, width, bold)
    if max_lines and len(lines) > max_lines:
        raise ValueError(f'Text requires {len(lines)} lines; limit is {max_lines}')
    leading = math.ceil(size * 1.28)
    for line in lines:
        draw.text((x, y), line, font=font(size, bold), fill=color, anchor='lt')
        y += leading
    return y


def configuration(path):
    c = read_json(path)
    if c['platform'] != 'linkedin' or c['language'] != 'en':
        raise ValueError('Only English LTR LinkedIn rendering is implemented')
    for name, ratio in [('slides', 4/5), ('video', 9/16)]:
        w, h = c[name]['width'], c[name]['height']
        if not isinstance(w, int) or not isinstance(h, int) or w < 1080 or abs(w/h-ratio) > 0.0001 or w % 2 or h % 2:
            raise ValueError(f'{name}: use even dimensions, width >=1080 and the documented aspect ratio')
    if c['video']['fps'] != 30:
        raise ValueError('This template uses 30 fps; retest motion/subtitles before changing fps')
    if not 0 <= c['video']['phrase_pause_seconds'] <= 1 or not 4 <= c['video']['min_scene_seconds'] <= 10:
        raise ValueError('Invalid narration padding settings')
    if c['integrations']['publishing'] != 'disabled; no implementation':
        raise ValueError('No publishing integration is implemented')
    output = Path(c['output_dir'])
    if output.is_absolute() or not (ROOT/'out').resolve() in (ROOT/output).resolve().parents:
        raise ValueError('output_dir must be a project-relative child of out/')
    for value in c['theme'].values():
        if not re.fullmatch(r'#[0-9A-Fa-f]{6}', value):
            raise ValueError('Theme colors must use #RRGGBB')
    return c


def new_job(c, kind):
    p = ROOT / c['output_dir'] / kind
    p.mkdir(parents=True, exist_ok=False)
    return p


def caption(data, job):
    if not data.get('caption') or not data.get('sources'):
        raise ValueError('Supply caption and public source records')
    urls = [s['url'] for s in data['sources']]
    if any(not url.startswith(('https://', 'http://')) for url in urls):
        raise ValueError('Sources must be public URLs, not local paths')
    text = data['caption'].rstrip()
    missing = [u for u in urls if u not in text]
    if missing:
        text += '\n\nSources:\n' + '\n'.join(missing)
    (job/'caption.md').write_text(text+'\n', encoding='utf-8')


def slides(data, c, pdf=False):
    if not 6 <= len(data['slides']) <= 8:
        raise ValueError('Slide posts require 6-8 slides')
    job = new_job(c, 'slides')
    palette = c['theme']; previews = []; bounds = []; outputs = []
    for index, s in enumerate(data['slides'], 1):
        im = Image.new('RGB', (1080,1350), palette['bg']); d = ImageDraw.Draw(im)
        text_block(d, s['section'], 76, 145, 928, 30, palette['cyan'], max_lines=1)
        y = text_block(d, s['title'], 76, 215, 928, 68, palette['white'], True, 3)+30
        y = text_block(d, s['intro'], 76, y, 928, 42, palette['muted'], max_lines=4)+36
        if len(s['cards']) != 2:
            raise ValueError('This compact template expects two cards')
        for card in s['cards']:
            label_size = card.get('label_size', 30)
            if not 30 <= label_size <= 60:
                raise ValueError('Card labels must be 30-60 px')
            label_bold = card.get('label_bold', False)
            label_lines = wrap(card['label'], label_size, 860, label_bold)
            body_lines = wrap(card['body'], 42, 860)
            height = 68+len(label_lines)*math.ceil(label_size*1.28)+18+len(body_lines)*54
            if y+height > 1180:
                raise ValueError(f'Slide {index} overflows; shorten copy, never shrink type')
            d.rounded_rectangle((76,y,1004,y+height),radius=16,fill=palette['panel'],outline=palette['line'],width=2)
            cy = text_block(d,card['label'],110,y+32,860,label_size,palette['amber'],label_bold,2)+18
            text_block(d,card['body'],110,cy,860,42,palette['white'],max_lines=4)
            y += height+24
        bounds.append({'slide':index,'content_bottom':y-24,'limit':1180})
        text_block(d, data['footer'], 76, 1225, 820, 24, palette['muted'], max_lines=1)
        d.text((1004,1225),f'{index:02}/{len(data["slides"]):02}',font=font(24),fill=palette['muted'],anchor='rt')
        d.rectangle((76,1290,1004,1295), fill=palette['line'])
        d.rectangle((76,1290,76+round(928*index/len(data['slides'])),1295),fill=palette['cyan'])
        final = im.resize((c['slides']['width'],c['slides']['height']),Image.Resampling.LANCZOS)
        name=f'slide-{index:02}.png'; final.save(job/name);outputs.append(name)
        mobile=final.resize((360,450),Image.Resampling.LANCZOS);mobile.save(job/f'mobile-{index:02}.png');previews.append(mobile)
        if index == 1: final.save(job/'cover.png')
    sheet=Image.new('RGB',(360*4,450*2),palette['bg'])
    for i,im in enumerate(previews):sheet.paste(im,((i%4)*360,(i//4)*450))
    sheet.save(job/'contact-sheet.png')
    if pdf:
        pages=[Image.open(job/n).convert('RGB') for n in outputs]
        pages[0].save(job/'slides.pdf',save_all=True,append_images=pages[1:],resolution=144)
    caption(data,job);write_json(job/'source.json',data)
    write_json(job/'validation.json',{'ordered_images':outputs,'dimensions':[c['slides']['width'],c['slides']['height']],'mode':'RGB','content_bounds':bounds,'header':'No internal project header is rendered','pdf_requested':pdf,'mobile_body_px':14,'visual_review':'pending human inspection','source_verification':'user/agent evidence review required; URL syntax is not fact verification'})
    return job


def write_wav(path, samples, rate):
    with wave.open(str(path),'wb') as out:
        out.setparams((1,2,rate,0,'NONE','not compressed'))
        if sys.byteorder != 'little':samples= array('h',samples);samples.byteswap()
        out.writeframes(samples.tobytes())


def read_wav(path):
    with wave.open(str(path),'rb') as w:
        if w.getnchannels()!=1 or w.getsampwidth()!=2 or w.getcomptype()!='NONE':
            raise ValueError('Supply mono, 16-bit uncompressed PCM WAV audio')
        rate=w.getframerate();a=array('h',w.readframes(w.getnframes()))
        if sys.byteorder!='little':a.byteswap()
    if not len(a) or max(abs(v) for v in a)==0:
        raise ValueError('Narration WAV is empty or silent')
    return a,rate


def timestamp(frames, fps):
    m=round(frames/fps*1000)
    return f'{m//3600000:02}:{m//60000%60:02}:{m//1000%60:02},{m%1000:03}'


def prepare_video(data,c,fixture=False, source_dir=None):
    provider='fixture' if fixture else c['tts']['provider']
    if provider not in ['fixture','wav','piper']:
        raise ValueError('Choose wav or piper; no hosted service is implemented')
    if provider!='fixture' and not c['tts']['rights_reviewed']:
        raise ValueError('Review the selected voice/recording rights and set tts.rights_reviewed=true')
    if not 5 <= len(data['video']['scenes']) <= 7:
        raise ValueError('Video requires 5-7 short scenes')
    model=os.environ.get('PIPER_MODEL')
    if provider=='piper' and (not model or not Path(model).is_file()):
        raise ValueError('Set PIPER_MODEL to an authorized local ONNX file; no download occurs')
    job=new_job(c,'video');pub=job/'public';pub.mkdir();shutil.copytree(FONTS,pub/'fonts')
    fps=c['video']['fps'];cursor=0;all_audio=array('h');scenes=[];cues=[];rate=None
    for i,scene in enumerate(data['video']['scenes']):
        parts=array('h');local_cues=[]
        for j,phrase in enumerate(scene['phrases']):
            if not phrase.strip():raise ValueError('Narration phrases must not be empty')
            lines=wrap(phrase,48,888,True)
            if len(lines)>2:raise ValueError('Split this phrase: subtitles exceed two measured lines')
            target=job/f'phrase-{i+1:02}-{j+1:02}.wav'
            if provider=='fixture':
                sr=22050;a=array('h',(round(1600*math.sin(2*math.pi*440*n/sr)) for n in range(round(sr*2.2))))
                write_wav(target,a,sr)
            elif provider=='wav':
                inputs=scene.get('audio_phrases',[])
                if len(inputs)!=len(scene['phrases']):raise ValueError('Supply audio_phrases with one WAV per phrase')
                source=(Path(source_dir)/inputs[j]).resolve();shutil.copyfile(source,target);a,sr=read_wav(target)
            else:
                command=[os.environ.get('PIPER_PYTHON',sys.executable),'-m','piper','--model',model,'--output-file',str(target),'--length-scale',str(c['tts']['length_scale']),'--noise-scale',str(c['tts']['noise_scale']),'--noise-w-scale',str(c['tts']['noise_w_scale'])]
                subprocess.run(command,input=phrase+'\n',encoding='utf-8',check=True,cwd=job,capture_output=True)
                a,sr=read_wav(target)
            if rate is None:rate=sr
            if sr!=rate:raise ValueError('All phrase WAVs must use the same sample rate')
            if not parts:parts.extend([0]*round(.20*rate))
            start=len(parts);parts.extend(a);end=len(parts)
            local_cues.append({'fromFrame':cursor+round(start/rate*fps),'toFrame':cursor+math.ceil(end/rate*fps),'text':'\n'.join(lines)})
            parts.extend([0]*round(c['video']['phrase_pause_seconds']*rate))
        if not parts:raise ValueError('Every scene requires narration phrases')
        frames=max(round(c['video']['min_scene_seconds']*fps),math.ceil((len(parts)/rate+.35)*fps))
        parts.extend([0]*(round(frames/fps*rate)-len(parts)))
        peak=max(abs(v) for v in parts);gain=min(1.0,28000/max(peak,1));parts=array('h',(round(v*gain) for v in parts))
        write_wav(pub/f'scene-{i+1:02}.wav',parts,rate);all_audio.extend(parts);cues.extend(local_cues)
        scenes.append({k:v for k,v in scene.items() if k not in ['phrases','audio_phrases']} | {'startFrame':cursor,'durationInFrames':frames,'audio':f'scene-{i+1:02}.wav','gain':gain})
        cursor+=frames
    if not 30<=cursor/fps<=60:raise ValueError(f'Narration is {cursor/fps:.2f}s; edit phrases or padding to reach 30-60s')
    if any(cues[i]['fromFrame']<cues[i-1]['toFrame'] for i in range(1,len(cues))):raise ValueError('Rounded subtitle cues overlap')
    timing={'title':data['title'],'exampleLabel':data['example_label'],'footer':data['footer'],'width':c['video']['width'],'height':c['video']['height'],'fps':fps,'durationInFrames':cursor,'theme':c['theme'],'scenes':scenes,'captions':cues,'audio_kind':'synthetic test tones; NOT narration' if fixture else 'speech','sampleRate':rate,'provider':provider}
    write_json(job/'timing.json',timing);write_json(job/'source.json',data);write_wav(job/'narration.wav',all_audio,rate)
    (job/'captions.en.srt').write_text('\n\n'.join(f'{i+1}\n{timestamp(x["fromFrame"],fps)} --> {timestamp(x["toFrame"],fps)}\n{x["text"]}' for i,x in enumerate(cues))+'\n',encoding='utf-8')
    (job/'voiceover.md').write_text('# Exact script\n\n'+'\n\n'.join(' '.join(s['phrases']) for s in data['video']['scenes'])+'\n',encoding='utf-8')
    caption(data,job)
    return job


def run(command):
    return subprocess.run([str(x) for x in command],check=True,capture_output=True)


def validate_video(job):
    ff=os.environ.get('FFMPEG','ffmpeg');probe=os.environ.get('FFPROBE','ffprobe');mp4=job/'motion.mp4';t=read_json(job/'timing.json')
    meta=json.loads(run([probe,'-v','error','-show_streams','-show_format','-of','json',mp4]).stdout)
    video=next(x for x in meta['streams'] if x['codec_type']=='video');audio=next(x for x in meta['streams'] if x['codec_type']=='audio')
    # Normalize full-range browser renders to common limited-range yuv420p if necessary.
    if video['pix_fmt']!='yuv420p' or video.get('color_range')=='pc':
        target=job/'normalized.mp4'
        run([ff,'-y','-v','error','-i',mp4,'-vf','scale=in_range=full:out_range=tv,format=yuv420p','-color_range','tv','-c:v','libx264','-crf','18','-preset','fast','-c:a','copy','-movflags','+faststart',target])
        target.replace(mp4)
        meta=json.loads(run([probe,'-v','error','-show_streams','-show_format','-of','json',mp4]).stdout)
        video=next(x for x in meta['streams'] if x['codec_type']=='video')
    duration=float(meta['format']['duration'])
    assert 30<=duration<=60 and abs(duration-t['durationInFrames']/t['fps'])<.1
    assert (video['width'],video['height'])==(t['width'],t['height'])
    assert video['codec_name']=='h264' and video['pix_fmt']=='yuv420p' and audio['codec_name']=='aac'
    run([ff,'-y','-v','error','-i',mp4,'-c:v','rawvideo','-c:a','pcm_s16le','-f','null','-'])
    decoded=job/'decoded-audio.wav';run([ff,'-y','-v','error','-i',mp4,'-vn','-ac','1','-ar',str(t['sampleRate']),'-c:a','pcm_s16le',decoded])
    samples,rate=read_wav(decoded);peak=max(abs(v) for v in samples)/32768;rms=math.sqrt(sum(v*v for v in samples)/len(samples))/32768
    assert rms>.003 and peak<.999,'Silent or clipped audio'
    reference,reference_rate=read_wav(job/'narration.wav')
    assert reference_rate==rate and abs(len(reference)-len(samples))/rate<.1
    matches=[]
    # Compare every scene with the exact prepared audio, allowing tiny clip-frame
    # alignment differences and lossy AAC. Subsampling keeps this standard-library only.
    for scene in t['scenes']:
        begin=round(scene['startFrame']/t['fps']*rate)+32
        end=min(round((scene['startFrame']+scene['durationInFrames'])/t['fps']*rate),len(samples),len(reference))-32
        positions=range(begin,end,16);energy=sum(reference[i]**2 for i in positions)
        best=-1.0
        for lag in range(-32,33):
            dot=sum(reference[i]*samples[i+lag] for i in positions)
            other=sum(samples[i+lag]**2 for i in positions)
            best=max(best,dot/math.sqrt(max(energy*other,1)))
        assert best>.85,'Final MP4 audio does not match prepared narration'
        matches.append(round(best,6))
    previews=[]
    for i,scene in enumerate(t['scenes']):
        cue=next(x for x in t['captions'] if x['fromFrame']>=scene['startFrame'])
        seconds=(cue['fromFrame']+cue['toFrame'])/(2*t['fps'])
        target=job/f'preview-{i+1:02}.png';run([ff,'-y','-v','error','-ss',str(seconds),'-i',mp4,'-frames:v','1','-vf','scale=360:640',target])
        previews.append(Image.open(target).convert('RGB'))
        if i==0:run([ff,'-y','-v','error','-ss',str(seconds),'-i',mp4,'-frames:v','1',job/'cover.png'])
    sheet=Image.new('RGB',(1080,640*math.ceil(len(previews)/3)))
    for i,im in enumerate(previews):sheet.paste(im,((i%3)*360,(i//3)*640))
    sheet.save(job/'contact-sheet.png')
    report={'duration_seconds':duration,'dimensions':[video['width'],video['height']],'fps':video['r_frame_rate'],'video_codec':video['codec_name'],'pixel_format':video['pix_fmt'],'audio_codec':audio['codec_name'],'audio_peak':peak,'audio_rms':rms,'per_scene_audio_correlation':matches,'audio_alignment_allowance_samples':32,'full_decode':'pass','subtitles':len(t['captions']),'max_subtitle_lines':max(len(x['text'].split('\n')) for x in t['captions']),'subtitle_mobile_px':16,'timing':'Measured phrase WAV samples; phrase-level cues, not word alignment','audio_kind':t['audio_kind'],'visual_review':'pending human inspection of actual MP4 frames','listening_review':'pending human review','source_verification':'separate evidence review required','sha256':hashlib.sha256(mp4.read_bytes()).hexdigest()}
    write_json(job/'validation.json',report)
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=['slides','prepare-video','render-video','validate-video']);p.add_argument('--config',default='config.example.json');p.add_argument('--source',default='examples/synthetic-demo.json');p.add_argument('--pdf',action='store_true');p.add_argument('--fixture-audio',action='store_true',help='Test tones only; never speech')
    args=p.parse_args();c=configuration(args.config);data=read_json(args.source)
    if args.command=='slides':job=slides(data,c,args.pdf)
    elif args.command=='prepare-video':job=prepare_video(data,c,args.fixture_audio,Path(args.source).resolve().parent)
    else:
        job=ROOT/c['output_dir']/'video'
        if args.command=='render-video':subprocess.run(['node',str(ROOT/'scripts/render_video.mjs'),str(job)],check=True,cwd=ROOT)
        validate_video(job)
    print(job.relative_to(ROOT).as_posix())

if __name__=='__main__':
    try:main()
    except (ValueError,AssertionError,FileExistsError) as exc:raise SystemExit(f'Production stopped: {exc}')
