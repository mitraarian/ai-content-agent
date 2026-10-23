# Validation performed on this prepared export

Current license/packaging status is in the final section below. Earlier sections
record checks and license status at their respective audit stages.

This is a local candidate with unresolved release licensing. No repository, commit,
push, account connection, paid service, social scheduling or publication was used.
Windows/Node 24.19.0/Python 3.14/Pillow 13.0.0 were exercised. Existing local speech,
browser and FFmpeg runtimes were supplied explicitly; none is in the source export.

## Passed checks

- `npm install --offline --ignore-scripts --no-audit --no-fund`: fresh isolated
  install from the existing local cache, 186 packages; lockfile pruned/generalized.
  No package installation modified the original working projects.
- `npm run check`: TypeScript passes. `node --check scripts/render_video.mjs` passes.
- Codex skill-creator quick_validate.py: new content-production SKILL.md is valid.
- `python tests/smoke.py`: seven correctly numbered RGB 1080x1350 PNGs, blank
  internal-header area, measured content bounds, public caption URLs, no default
  PDF, 12 nonoverlapping sample-measured cues, two subtitle lines maximum.
  Unsupported language, output traversal and unbreakable overflowing text rejected.
  Fixture audio is explicitly test tones, never misreported as speech.
- Actual local speech was generated only from the synthetic tile-sorter example,
  using an explicitly supplied optional Piper 1.8.0 voice; all 12 phrase WAVs and
  frame/sample timing assertions passed. The initial full-video test encountered
  a localhost IPv4/IPv6 collision. After the render-port fix, the prepared job was
  resumed through the documented render-video command without regenerating audio.
- Completed speech MP4: **37.675 seconds, 1080x1920, 30fps, H.264/yuv420p, AAC**.
  Full frame/audio decode passes. Decoded audio peak 0.61145, RMS 0.08434; no
  silence/clipping indicated. Source-audio correlation by scene: 0.999877,
  0.958476, 0.999892, 0.999850, 0.973617, 0.999934, allowing 32 samples of
  clip-boundary alignment difference. These measure signal matching, not pronunciation.
- After adding the final subtitle DOM guard, 18 current-renderer frames (all 12
  subtitle positions plus six transition starts) rendered successfully with text
  and subtitle safe-area checks. This guard adds validation and does not change
  the completed video's visual layout.
- Assistant visual self-inspection: all seven 360px-wide slide previews and six
  final-MP4 frames at each of two subtitle positions per scene; clear reading order,
  no clipped main text or overlapping subtitles. Transition preview sheet inspected.
  Body copy is 14px at 360px slide width; video subtitles are 16px at 360px width.
- Explicit source allowlist and additional scan against 156 private topic/caption
  phrases pass: no known private phrases, credential patterns or personal absolute
  paths in proposed source. No Git/history, private content, downloaded voice,
  browser, dependency tree, generated media or stock asset enters the source archive.
  All 755 baseline-protected original source/content/media/Git files were preserved
  in the final check; the separate private audit contains detailed proof.

## Packaging and limits

Only the files enumerated by scripts/audit_export.py belong in the source release.
Synthetic test outputs were written under ignored out/ and are retained separately
for local review. Installed test dependencies and bytecode caches were removed from
the clean source folder after validation. Run the documented installation commands
before running it again. Privacy scans are heuristic, supplemented here by manual
review, file/category inventory, Git-object review and exact export allowlisting.

Human listening/naturalness/pronunciation review was not independently performed.
Original-code ownership and public licensing remain unconfirmed; no MIT LICENSE
was applied. The media-package license classification has since been resolved from pinned
upstream documentation. Complete native-bundle redistribution terms remain
unverified; this source distribution contains no native binaries. Custom Remotion
use terms and optional voice/output rights remain separate from original-code
licensing. See RELEASE-READINESS.md for the current source-release decision.
Persian/RTL, Instagram-specific layout, word alignment, automatic crawling/fact
checking and hosted TTS are not implemented. macOS/Linux and non-default dimensions
were not independently exercised. Optional raster PDF is implemented but was not
part of this minimal smoke test. See THIRD_PARTY_NOTICES.md and
LICENSE-RECOMMENDATION.md before any public release.

## Earlier release audit reproduction

An isolated copy of the original source ZIP was used, without changing either
working project or installing dependencies in this clean source folder:

- Fresh Python environment plus `pip install -r requirements.txt` from official
  PyPI: pass (Pillow 13.0.0).
- `npm ci --offline --ignore-scripts --no-audit --no-fund` from the existing cache,
  then `npm run check`: pass. This verifies lockfile consistency and a fresh local
  install, not a cold-cache network install on every operating system.
- `python tests/smoke.py` and `python tests/smoke.py --video`: pass end to end.
  The latter creates a 32-second 1080x1920 H.264/yuv420p + AAC fixture with 12
  timed cues, full decode and audio-match checks. It contains explicitly labeled
  test tones, not speech. An existing browser/FFmpeg installation was supplied.
- The earlier real-speech MP4's hash still matches its successful validation.
  Optional Piper installation/synthesis was not repeated; human listening is pending.
- All 28 physical source files match the explicit export allowlist. No ignored
  directories, generated media, dependency trees, voices, recordings, Git history
  or symlinks are present. Heuristic secret/path scans and comparisons against
  181 private topic/caption phrases pass, including all 25 backlog candidates.
- The original 27-file ZIP was verified and retained unchanged. The refreshed
  28-file reviewed source ZIP includes the final documentation/metadata fixes.
  Both archives exclude personal content and the separate private audit folder.

The renderer, narration code, configuration, tests, skill, package.json and lockfile
were unchanged by that earlier audit. Its only script edit adds this release report to the
export allowlist. The recommendation is still NO-GO pending original-code rights
and approved licensing; no copyright holder or legal clearance was invented.

## Bootstrap/config replacement: fresh reproduction

The follow-up replaces only src/index.ts and tsconfig.json, plus the three audit
and notice documents. The engine, composition/design, fonts, dependencies, tests,
configuration example and private-data exclusions are unchanged by SHA-256.

A newly copied source tree, fresh Python environment/Pillow install from official
PyPI, and locked `npm ci --offline --ignore-scripts --no-audit --no-fund` (186
packages from the existing cache) pass. `npm run check`, Node syntax check,
`python tests/smoke.py` and `python tests/smoke.py --video` all pass. Existing
browser/FFmpeg executables were supplied; no runtime was bundled or purchased.

The standalone and full-video runs each export seven ordered RGB 1080x1350 slides,
with blank internal-header margin and measured text bounds; all fourteen PNGs are
byte-identical to their earlier smoke counterparts. The fresh MP4 is 32.021s,
1080x1920/30fps, H.264/yuv420p + AAC. Full decode, non-silent/unclipped audio,
12 sample-timed subtitle cues (two lines maximum) and all six audio-match checks
pass (minimum correlation 0.999031). Its hash matches the prior fixture exactly:
`77ea957c001638fb5ca684508e714d7ad7b15e8afb66f54210978bd3a3cc176e`.
Audio is explicitly synthetic test tones, not speech. Optional Piper synthesis and
human listening were not repeated. Assistant inspection of seven 360px slide
previews and six MP4-derived scene previews found readable text without clipping;
subtitle size is 16px at 360px video width. Automated DOM safe-area guards also pass.

Final source allowlist/secret-path scans and 181 private-phrase comparisons pass;
all 28 source files are accounted for, with no dependencies, generated outputs,
models, recordings, Git history or private audit files in the source candidate.
All 755 protected original-file baseline hashes still match. Requirements, logs,
before/after evidence and renders are held only in the separate private audit.
Historical ZIPs are untouched and stale; they are not updated release artifacts.
This validates functionality/preservation, not ownership, legal rights, every-frame
visual review, pronunciation or operating systems other than the tested Windows
configuration. RELEASE-READINESS.md retains the current NO-GO and remaining blockers.

## Scoped MIT license and final source packaging

The project owner explicitly supplied Copyright (c) 2026 Mitra Arian and approved
MIT only for original code/documentation within the rights held. LICENSE is now
included in the explicit source allowlist; package.json/root lock metadata agree.
The complete Sergey Bulaev MIT notice and all Vera font files/notices are unchanged.

Final source and reopened ZIP checks pass: exactly 29 allowlisted files, CRC and
per-entry SHA-256 equality, no symlinks/Git/dependencies/generated outputs, secret
and private-path checks, and comparisons against 181 private topic/caption phrases.
The synthetic demo's fictional caption is intentionally included; no personal
posts/captions, research/backlog/topics, media outputs, voices, recordings or
credentials are included. All 755 protected original-file hashes and earlier ZIPs
still match. The source-only ZIP excludes the separate private audit directory.

Production code/designs/tests/dependency versions are unchanged from the fresh
TypeScript/carousel/full-video smoke results above. Those expensive functional
checks were not repeated for license/docs/root-metadata and export-allowlist edits.
The final source audit, Python syntax and package/lock consistency were checked.
Technical packaging does not certify ownership beyond the rights actually held,
Remotion eligibility or optional voice/output rights. No remote action was taken.
