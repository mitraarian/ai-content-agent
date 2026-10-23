# AI Content Production Agent

A small local content-production engine for Codex: research/write through a
portable skill, render ordered PNG slide posts, and render narrated Remotion MP4s
with audio-derived English subtitles. No web app, social account connection,
automatic publishing, paid API or hosted text generator is included.

**License:** [MIT](LICENSE) for the original project code and documentation,
Copyright (c) 2026 Mitra Arian, only to the extent Mitra Arian owns the rights to
those portions. The attribution was explicitly supplied by the project owner;
this is not an independent certification of ownership of every contribution.

Third-party material remains under its own terms. The retained LinkedIn guidance
keeps Sergey Bulaev's original MIT notice; the bundled Vera fonts retain their
separate font license. Remotion, FFmpeg, optional Piper, React, Pillow and other
external dependencies are not relicensed by LICENSE. Preserve
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and the complete font notice.

**Release status:** local source candidate; `private: true` still prevents accidental
npm publication. License approval does not authorize publication or resolve unknown
contributor/employer rights. See [RELEASE-READINESS.md](RELEASE-READINESS.md) for
packaging results and remaining provenance/use limitations.

## What actually works

- English LinkedIn multi-image posts: 6-8 RGB PNGs, default 1080x1350, ordered
  `slide-01.png` onward, caption.md, editable source, cover, mobile previews and
  measured text-bound validation. No internal project header.
- English 30-60s motion videos: 5-7 scenes, 1080x1920/30fps, H.264/yuv420p + AAC,
  phrase-level burned-in subtitles, SRT, WAV narration, timing JSON, cover and
  final-MP4-derived previews. Use an explicitly chosen local Piper voice, or supply
  one mono 16-bit PCM WAV per phrase. Nothing is silently downloaded.
- Configurable colors, label typography, supported dimensions, local output folder
  and speech settings. Cadence/timezone/schedule are **editorial instructions for
  the agent**, not a scheduling service. Caption/source verification needs research
  and human judgment; the renderer only checks source URL syntax.
- Optional raster PDF via `slides --pdf`; PNG is the primary deliverable.

Persian/RTL, Instagram-specific adaptations, automatic topic scraping, automatic
fact checking, word alignment and hosted TTS are **not implemented**. Unsupported
platform/language settings fail explicitly. The portable skill documents research
and localization requirements; instructions do not constitute tested renderers.

## Prerequisites and setup

Use Node 24 (or the versions in package.json) and Python 3.11+ (3.13 recommended
for optional speech wheels). Windows is tested; macOS/Linux installation is not
independently tested. Install your own authorized Chrome/Chromium and FFmpeg with
H.264/AAC support plus ffprobe for video. No browser, voice, stock media, original
recording or dependency tree is distributed. Slides need only Python and Pillow.
The included unmodified Vera fonts have their complete license beside them.

Review [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) first. Remotion has a
custom license: its pinned 4.x terms provide a free tier for eligible individuals,
small organizations and nonprofits, and require a company license for other uses.
This engine cannot guarantee free Remotion use for every organization. It never
buys a license or calls a paid service. Installation uses your package registries
and network; rendering uses installed local tools. `npm ci` installs native
Remotion platform packages, including FFmpeg, even with `--ignore-scripts`.
Those are external dependencies, not binaries included in this source archive.
Their licenses remain separate from the scoped MIT license of our original code.
FFMPEG/FFPROBE select tools for Python validation; Remotion rendering uses its
installed platform binaries. Browser and voice acquisition remain explicit.

From this folder:

```sh
python -m venv .venv
# Activate the environment using your shell's normal activation command.
python -m pip install -r requirements.txt
npm ci --ignore-scripts
npm run check
python tests/smoke.py
```

On Windows, if `python` opens the Store, use `py -3.13` to create the environment,
then `.venv\Scripts\python.exe` for Python commands. Activate with
`.venv\Scripts\Activate.ps1` (PowerShell) or `source .venv/bin/activate` (POSIX).
A browser/runtime dependency that requires installation must be explicitly
installed by you; the renderer refuses an absent browser rather than fetching one.

## Render the synthetic slides

```sh
python scripts/content.py slides --config config.example.json --source examples/synthetic-demo.json
```

Output: `out/demo/slides/`. Upload `slide-01.png` through `slide-07.png` in order,
then paste caption.md. Do not upload mobile previews or the contact sheet.
Inspect contact-sheet.png and the 360px previews before using real content.
To request an optional raster PDF, add `--pdf` to a **new** render job. The PDF
has image pages, not selectable text; its ordered source PNGs remain primary.

Existing job folders are preserved. For revisions create `.local/` if absent, then copy config.example.json to
`.local/config.json` and change output_dir, e.g. `out/my-revision`, before rendering.
Do not delete an approved package merely to make a command rerun.

## Render a narrated video

The default `tts.provider: wav` deliberately requires supplied recordings; there
is no default narrator. For Piper, optionally install the separately licensed tool:

```sh
python -m pip install -r requirements-tts.txt
```

Obtain an authorized ONNX model and its matching .onnx.json separately from the
[voice catalog](https://huggingface.co/rhasspy/piper-voices). Review the exact model
card, dataset, speaker/personality rights and intended use; a catalog-wide MIT tag
is not complete output-rights clearance. Nothing downloads a voice for you.
Copy config.example.json to `.local/config.json`; set `tts.provider` to `piper`
and `tts.rights_reviewed` to true only after your review. Choose output_dir for the
new job. Export these variables (the .env.example file is documentation, not loaded):

```powershell
$env:PIPER_MODEL = (Resolve-Path 'models/authorized-voice.onnx').Path
$env:PIPER_PYTHON = (Resolve-Path '.venv/Scripts/python.exe').Path
$env:CONTENT_AGENT_BROWSER = 'path-to-your-installed-chrome-executable'
$env:FFMPEG = 'ffmpeg'
$env:FFPROBE = 'ffprobe'
```

In a POSIX shell use `export NAME=value` instead. FFmpeg/ffprobe must be on PATH
or set to explicit executable paths. PIPER_PYTHON can select a separate supported
speech environment. Paths belong in shell/private configuration, never committed.

```sh
python scripts/content.py prepare-video --config .local/config.json --source examples/synthetic-demo.json
python scripts/content.py render-video --config .local/config.json --source examples/synthetic-demo.json
```

For recorded narration keep provider `wav`. Add an `audio_phrases` list beside
each scene's `phrases` in your private source JSON, one WAV per phrase, relative
to that JSON's folder. All WAVs must be mono, uncompressed PCM, 16-bit and the
same sample rate. A phrase recording should contain only that phrase; internal
silence is included in its subtitle interval. Rights review is required here too.

Output: `out/<job>/video/motion.mp4`, narration.wav, scene/phrase WAVs,
captions.en.srt, timing.json, voiceover.md, caption.md, source.json, validation.json,
cover.png and contact-sheet.png. The temporary bundle/public inputs stay inside
the same ignored job. The Python render-video command runs final validation and
normalizes full-range pixels if necessary. Standalone `npm run render:video --
out/<job>/video` renders only; then run the Python validate-video command.

Timing is measured from synthesized/recorded samples, not estimated word counts.
Subtitles are phrase-level (maximum two measured lines), not karaoke word timing.
If runtime exceeds 60s, shorten phrases; do not clip speech. If below 30s, revise
script/padding. Narration is peak-limited, not a claim of broadcast loudness
compliance. Listen and review pronunciation/synchronization before release.

## Smoke checks

```sh
python tests/smoke.py
# Optional full pipeline, test tones explicitly labeled NOT narration:
python tests/smoke.py --video
# Optional actual speech after the explicit voice configuration above:
python tests/smoke.py --video --speech --config .local/config.json
```

Tests write new ignored `out/smoke-.../` jobs: seven PNG dimensions/order,
header-free top margin, readable measured bounds, sample-timed cues, two lines,
output-traversal rejection and unsupported-language rejection. Video mode checks
H.264/AAC streams, duration, pixel format, full decode and non-silent unclipped
signal, per-scene audio matching against the prepared WAV (32-sample alignment
allowance), and derives review images from the MP4. It does not automatically verify
facts, pronunciation, rights, visual semantics or creative quality. A tone-only
fixture is never a completed narrated post. See VALIDATION.md for checks actually
performed on this export.

## Configuration and content contract

`config.example.json` is the single example; copy it to an ignored private path.
`examples/synthetic-demo.json` is the small editable content schema. It is clearly
fictional, contains no real monthly selection/research and makes no deployment claim.

| Field | Effect |
|---|---|
| platform / language | Renderer supports linkedin / en only; other values fail |
| cadence / timezone / schedule | Agent planning preferences; never social scheduling |
| formats | Agent's requested mix; run explicit CLI commands for actual exports |
| output_dir | Relative child of out/; originals/external paths cannot be output targets |
| slides width / height | 4:5, even dimensions, width >=1080; scales the base layout |
| video width / height / fps | 9:16, even dimensions, width >=1080, 30fps |
| video min_scene_seconds / phrase_pause_seconds | Padding derived around measured speech |
| theme | Seven #RRGGBB colors; retain contrast when changing |
| tts provider | wav or optional separately installed piper |
| tts rights_reviewed | Explicit local confirmation; not legal certification |
| integrations | Optional writing guidance reference only; publishing absent |
| cards label_size / label_bold | Source JSON: 30-60px label size and optional bold |

The renderer uses licensed Vera Regular/Bold for reproducible Latin text. Font
substitution/localization requires code changes and separate glyph/RTL QA.
Overflow raises an error: shorten copy or revise the template rather than shrink
mobile text. No main content enters the top 110px slide margin.

## Codex and optional LinkedIn writing skills

Open this project in Codex. AGENTS.md points to the discoverable
`.agents/skills/content-production/SKILL.md`. Ask it to prepare a local package
using your private brief/configuration. The skill uses a local private backlog,
monthly three-platform discovery, primary-source verification, captions and QC.
Research and drafting require the user's chosen agent/model/tool access; they
are not an embedded autonomous crawler or an included free LLM service.

Optionally obtain [linkedin-skills](https://github.com/sergebulaev/linkedin-skills)
separately and set LINKEDIN_SKILLS_DIR. Its observed license is MIT; retain its
notices if redistributing it. Read its own AGENTS.md and load planner, writer,
humanizer or repurposer instructions by reference as needed. It is not bundled,
a required render dependency, or automatically invoked by these Python commands.
Do not import private voice profiles, story banks, analytics or account settings.
Ignore conflicting publishing/paid-service defaults without explicit authorization.

## Troubleshooting

- Existing job: choose a fresh output_dir; files are preserved by default.
- Text overflow: reduce copy, split a phrase, or adjust the template and rerun QC.
- Missing speech/model: install the optional runtime yourself, set model/interpreter
  variables, check its matching JSON and review rights. No automatic downloads.
- Missing browser: set CONTENT_AGENT_BROWSER to an existing compatible executable.
- FFmpeg failure: select a build with H.264/AAC plus matching ffprobe; licenses and
  codec patent obligations depend on your build/use. No binary is redistributed.
- Python errors: use the environment where Pillow is installed; optional Piper can
  use another interpreter. Do not use the system Store placeholder as Python.
- A failed job may leave partial files for diagnosis. Keep it private and use a
  fresh job for retries; never label a partial export complete.
- Cross-platform differences: Windows was exercised here; test your own platform
  and dependency/browser versions before promising reproducible production.

## Source-only export audit

Run `python scripts/audit_export.py` before preparing a source release. It checks
an explicit allowlist, rejects unlisted source files, excludes all Git metadata,
scans for common secrets and personal paths, and writes `out/source-manifest.json`. Only listed
source files belong in a release; never upload the entire local folder or ignored
smoke media. Pattern checks do not replace manual privacy/provenance review.
