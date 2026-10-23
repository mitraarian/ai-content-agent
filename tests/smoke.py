"""Synthetic local smoke: PNG layout, sample timing, SRT and failure boundaries.
Optional --video needs installed Remotion/browser/FFmpeg. Default uses test tones,
explicitly not narration. --speech uses the configured authorized speech provider.
"""
from pathlib import Path
import argparse, copy, importlib.util, json, os, subprocess, sys, uuid
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('engine',ROOT/'scripts/content.py');engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--video',action='store_true');p.add_argument('--speech',action='store_true');p.add_argument('--config',default=str(ROOT/'config.example.json'));args=p.parse_args()
c=engine.configuration(args.config);c['output_dir']='out/smoke-'+uuid.uuid4().hex[:8];data=engine.read_json(ROOT/'examples/synthetic-demo.json')
slides=engine.slides(data,c);images=sorted(slides.glob('slide-*.png'))
assert [p.name for p in images]==[f'slide-{i:02}.png' for i in range(1,8)]
for f in images:
 with Image.open(f) as im:
  assert im.size==(1080,1350) and im.mode=='RGB'
  assert im.crop((0,0,1080,110)).getextrema()==((7,7),(17,17),(31,31)), 'Unexpected top header'
assert not list(slides.glob('*.pdf'))
assert 'https://' in (slides/'caption.md').read_text(encoding='utf-8')
timing_job=engine.prepare_video(data,c,fixture=not args.speech,source_dir=ROOT/'examples');t=engine.read_json(timing_job/'timing.json')
assert 900<=t['durationInFrames']<=1800 and len(t['captions'])==12
assert all(len(x['text'].split('\n'))<=2 for x in t['captions'])
assert all(x['fromFrame']<x['toFrame'] for x in t['captions'])
assert all(t['captions'][i-1]['toFrame']<=t['captions'][i]['fromFrame'] for i in range(1,12))
assert t['audio_kind']==('speech' if args.speech else 'synthetic test tones; NOT narration')
# Check measured timing against each separately saved phrase's sample count.
for i,scene in enumerate(t['scenes']):
 for j in range(2):
  samples,rate=engine.read_wav(timing_job/f'phrase-{i+1:02}-{j+1:02}.wav');cue=t['captions'][i*2+j]
  assert abs((cue['toFrame']-cue['fromFrame'])/30-len(samples)/rate)<2/30
for change in [('language','fa'),('output_dir','../outside')]:
 bad=copy.deepcopy(c);bad[change[0]]=change[1];f=ROOT/c['output_dir']/f'invalid-{change[0]}.json';engine.write_json(f,bad)
 try:engine.configuration(f)
 except ValueError:pass
 else:raise AssertionError('Unsupported configuration accepted')
try:engine.wrap('too_long_'*200,42,100)
except ValueError:pass
else:raise AssertionError('Unbreakable overflowing text accepted')
if args.video:
 subprocess.run(['node',str(ROOT/'scripts/render_video.mjs'),str(timing_job)],check=True,cwd=ROOT)
 engine.validate_video(timing_job)
report={'result':'PASS','slide_count':len(images),'dimensions':[1080,1350],'header_absent':True,'duration_seconds':t['durationInFrames']/30,'subtitle_cues':len(t['captions']),'audio_kind':t['audio_kind'],'video_rendered':args.video,'timing_samples_checked':True,'negative_checks':['unsupported language','output traversal','unbreakable text'],'visual_and_listening_review':'not automated; inspect exported previews and listen to actual narration'}
engine.write_json(ROOT/c['output_dir']/'smoke-result.json',report)
print(json.dumps(report,indent=2));print('Output: '+c['output_dir'])
