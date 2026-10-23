# Release readiness and provenance

**Scoped MIT applied; privacy/packaging PASS.** The project owner explicitly supplied
**Copyright (c) 2026 Mitra Arian** and approved the standard [MIT LICENSE](LICENSE)
for original code/documentation only to the extent of rights held. package.json and
root lock metadata now declare MIT; package.json remains private. This resolves the
license choice and attribution without asserting ownership of every contribution.

**NO-GO for an unqualified claim of full rights clearance.** Rights in any original/local
contribution outside Mitra Arian's ownership remain unverified and are not granted.
The identified starter implementation has been replaced and tested, without a
clean-room certification. Third-party notices/licenses remain separate. The local
source-only package passes technical packaging checks; no public release is authorized.

## Exact LinkedIn upstream

The original fork's GitHub parent and source are both
[sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills), not a
separately authored engine. The local checkout HEAD is upstream commit
`261240ac5c4da8b4465cbd364d14ce52ffed12ce` (v1.1.23), tree
`efb9de4301a4cc428e90ae4ffca2f200ddad99e9`. Its
[actual license](https://github.com/sergebulaev/linkedin-skills/blob/261240ac5c4da8b4465cbd364d14ce52ffed12ce/LICENSE)
is MIT, with **Copyright (c) 2026 Sergey Bulaev**. GitHub fork lineage, commit/tree
and the immutable license were verified; private fork-account details stay outside
this public report. All 213 upstream regular files match the local tracked versions
after line-ending normalization, and all 12 upstream symlink targets match the local
representations. Fifteen local editorial-policy/template/fixture additions are not
in that upstream commit; location inside a fork does not establish their authorship
or license grant.

## Comparison method and scope

The 28 pre-license files were compared against the immutable upstream archive, the existing
local projects and the installed font source: SHA-256 equality, matching normalized
lines, 12-word sequences, exact line blocks and manual review of the known production
chain. The export's creation record identifies new AI-assisted drafts separately
from local adaptations. This is a bounded provenance review, not exhaustive internet
plagiarism detection, proof of independent creation or a legal copyrightability ruling.

At audit entry, no whole LinkedIn upstream file was copied into the 28-file package.
No substantive verbatim upstream skill body, hook catalog, client implementation,
template collection or visual/media asset was detected. The incidental common Python
ROOT idiom is not evidence of copying; shared permissive-license wording in the Vera
notice is not evidence that the font came from the LinkedIn repository.

The production brief explicitly reused upstream planner/writer/humanizer/repurposer
guidance. Its generated public adaptation is therefore recorded as **adapted/informed**,
not asserted to be uninfluenced original prose. Missing exact matches cannot exclude
protected adaptations. A complete upstream MIT notice is now retained conservatively
in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), without claiming that every new
engine file is an upstream derivative or assigning the new work to the upstream author.

## File-by-file provenance: all 29 source files

C = copied third-party material; A = local adaptation; G = generated metadata;
N = newly drafted/implemented with AI assistance; S = starter scaffold. N identifies
the observed production process, not legal ownership, originality or protectability.

| File | Class | Traceable source / treatment |
|---|---|---|
| `.agents/skills/content-production/SKILL.md` | A + N | Generated adaptation of the local production brief and editorial policy; optional upstream planner/writer/humanizer/repurposer guidance informs the integration. Not independently sourced from nothing. No substantive upstream verbatim body detected; retain conservative upstream notice and confirm local-brief rights. |
| `.env.example` | N | New documentation of environment variables actually used by the engine. Original-project candidate; no credentials, account details or vendor implementation. |
| `.gitignore` | A + N | New expanded exclusion list using the studio configuration and release requirements. Common configuration; not an upstream LinkedIn file copy. |
| `AGENTS.md` | A + N | Portable adaptation of the local entry points and production requirements. Original integration candidate with indirect LinkedIn-guidance influence; conservative acknowledgement retained. |
| `config.example.json` | A + G | Generated schema/default example from the local brief, studio palette and implemented CLI. Cadence/colors are reused local design inputs; no private topics or fixed narrator. Confirm local-design rights. |
| `CONTRIBUTING.md` | N | New export-specific contribution and validation instructions. Original-project candidate; not copied from upstream AGENTS.md or its commit-author rules. |
| `LICENSE` | C + N | Standard MIT license text; Copyright (c) 2026 Mitra Arian explicitly supplied by the project owner, for original portions only to the extent of rights held. No third-party ownership or independent legal verification is asserted. |
| `LICENSE-RECOMMENDATION.md` | N | Authored analysis updated to record the approved scoped MIT decision and its limits; preserves the earlier MIT/Apache comparison. |
| `package.json` | A + G (historical S facts) | Engine manifest retains the dependency versions and Node compatibility range traced through the studio scaffold. These are dependency/compatibility facts, not vendor implementation. Dependency/support declarations are unchanged; only root license metadata is updated to scoped MIT. Historical lineage remains acknowledged. |
| `package-lock.json` | A + G | Pruned/regenerated from the studio npm lock; many dependency records retained verbatim. Generated registry metadata, not independently authored library code and not a grant to redistribute dependency binaries. |
| `README.md` | N | New implementation/setup documentation, with explicit external documentation links. Original-project candidate; upstream template logo/README body was not carried over. |
| `RELEASE-READINESS.md` | N | New local release audit and this provenance assessment. Original-project candidate; reports evidence, not legal ownership clearance. |
| `requirements-tts.txt` | N + G | New optional Piper version declaration and license comment. No Piper source/model; runtime and voice terms remain separate. |
| `requirements.txt` | N + G | New Pillow version declaration. Dependency metadata only; no Pillow implementation vendored. |
| `THIRD_PARTY_NOTICES.md` | N + C | New compliance analysis; this audit adds the exact verified upstream MIT notice for conservative workflow attribution. The notice is third-party material, not our project license. Preserve it and the independent font notice. |
| `tsconfig.json` | N (replaces A + S) | Reconstructed from this engine's type-checking requirements: explicit entry/import graph, ESNext modules, bundler resolution, browser/React typing and strict no-emit checks. Prior scaffold configuration is superseded; shared option names/functional values remain. No clean-room or copyrightability conclusion. |
| `VALIDATION.md` | N + G | New descriptions of actual local smoke, privacy and media checks. Original-project candidate based on generated measurements; not upstream evaluation fixtures. |
| `docs/dependency-licenses.json` | G + N | Generated installed-package metadata inventory plus authored upstream review annotations. Contains names/versions/license findings, not vendored dependency source. |
| `examples/synthetic-demo.json` | N | New AI-assisted fictional tile-sorter script and caption created for this export. Original-project candidate; no private posts, research candidates or upstream creator story reused. |
| `public/README.md` | N | New asset-directory policy. Original-project candidate. |
| `public/fonts/bitstream-vera-license.txt` | C | Exact copy from the installed ReportLab font directory; byte-matches the cited upstream font notice. Bitstream Vera notice, not MIT project work; keep the complete text. |
| `public/fonts/Vera.ttf` | C | Exact unmodified Bitstream Vera Regular font from the installed ReportLab font directory. Third-party font, SHA-256 c4c45690b345435b2cba52ecabe275f05e49b389b39fe68ad03afbb551288d3d; retain its license. |
| `public/fonts/VeraBd.ttf` | C | Exact unmodified Bitstream Vera Bold font from the installed ReportLab font directory. Third-party font, SHA-256 cc037385e4d55bfde89b13e03091ee93bf40c0c52ddd391ff031ab276f13b8e9; retain its license. |
| `scripts/audit_export.py` | N + A | New export allowlist and scanning code, using common Python idioms and local preservation-check concepts. Original-project candidate. Shared ROOT path idiom alone is not evidence of upstream LinkedIn implementation copying. |
| `scripts/content.py` | A + N | Adapted studio measured-wrap/card layout, sample-timed narration/SRT, FFmpeg normalization and media-QC algorithms; direct Pillow PNG and external TTS interface newly implemented. Substantial local adaptation, not wholly independent code. Confirm rights to local implementations; no ReportLab/PyMuPDF/Piper implementation copied was identified. |
| `scripts/render_video.mjs` | N + A | New Node API wrapper replacing the studio dated render loop; own per-job bundling and local port handling. Uses Remotion APIs as dependencies; no SDK implementation is vendored. Local-code provenance still needs owner confirmation. |
| `src/index.ts` | N (replaces A + S) | New minimal React-element adapter registers a local catalog component that renders the unchanged Root. Written from the documented API/engine contract, not another starter or a rename of the old three-line bootstrap. Common API imports remain; historical lineage is retained below, without claiming legally proven independence. |
| `src/Root.tsx` | A + N | Adapted studio MonthlyMotion scene/card/caption/progress layout and Composition palette/spring reveals; added generic props, fonts and bounds checks. Substantial local implementation adaptation. Remotion API usage is distinct from copying vendor internals; local rights/provenance remain unconfirmed. |
| `tests/smoke.py` | N + A | New synthetic test harness adapting local dimension, timing and media-QC assertions. Not upstream LinkedIn test code or fixture data; confirm local-source rights for adapted portions. |

## Included third-party material and obligations

1. **Bitstream Vera:** both TTFs and the full license are exact copies from a ReportLab
   installation, independently byte-matched to the cited upstream font files. Keep
   `public/fonts/bitstream-vera-license.txt`, including copyright/trademark and
   permission notices. The license permits bundled redistribution; fonts cannot be
   sold alone, and modified fonts must follow its naming restrictions. Do not put
   these binaries under a new original-code license. ReportLab itself is not vendored.
2. **LinkedIn guidance:** conservative retained MIT notice covers any protectable
   upstream guidance adapted through the local brief; retain the actual upstream
   copyright and permission notice in copies/substantial portions, including modified
   prompt/instruction text. MIT permits reuse subject to its conditions; no separate
   permission is needed for uses that comply. Independently created local additions
   are not automatically upstream-owned or licensed merely by residing in the fork.
   This audit intentionally added the notice text; it was not a vendored runtime.
3. **Remotion scaffold: practical replacement completed.** Historical source is
   [template-empty at `bad1be9984b0`](https://github.com/remotion-dev/template-empty/tree/bad1be9984b08a9ee3f3eee1df98765caa04ca11).
   Its index/config matched the original studio, and its staged empty Root/Composition
   also matched. The public candidate retained only adapted bootstrap/config code and
   manifest compatibility facts; the blank scene, logo and template README were absent.
   The template metadata says UNLICENSED, with no standalone license found; its README
   points to Remotion terms. That history is preserved rather than assigned an MIT grant.

   The old public bootstrap is replaced with a newly written React-element adapter:
   register one catalog component at entry evaluation; let that component construct
   the existing Root with createElement. Registration stays outside the editable catalog
   as required by the [Remotion API](https://www.remotion.dev/docs/register-root).
   [React's element API](https://react.dev/reference/react/createElement) permits retaining
   the .ts entry without JSX or changes to the visual engine. No template implementation
   or documentation example was used as replacement text; required API imports overlap.

   The compiler configuration was reconstructed from an explicit requirements record:
   entry-file allowlist plus its import graph; no emitted output; strict/unused-local
   checks; ES2020 and browser iterable types; React automatic JSX. ESNext replaces
   Preserve for this ES-module-only bundle; explicit synthetic-default-import typing
   replaces esModuleInterop because TypeScript emits no runtime helpers. React ambient
   types are explicit; external declaration-file checking remains skipped as before.
   These choices use the [TypeScript module](https://www.typescriptlang.org/tsconfig/module.html),
   [bundler resolution](https://www.typescriptlang.org/tsconfig/moduleResolution.html),
   [entry allowlist](https://www.typescriptlang.org/tsconfig/files.html) and
   [default-import typing](https://www.typescriptlang.org/tsconfig/allowSyntheticDefaultImports.html)
   contracts. Shared configuration keys are functional settings; they were not changed
   arbitrarily to defeat a similarity check. Dependency versions, the lockfile and Node
   compatibility range remain unchanged as metadata, with their history acknowledged.

   This is a requirements-based, AI-assisted implementation after the old code had been
   seen, **not a clean-room process**. A wrapper, renamed identifier or reduced match
   score alone cannot extinguish third-party rights. The identified inherited bootstrap
   implementation/configuration has been superseded; no broader template-code grant is
   claimed. Protectability or rights in common API/configuration fragments is not legally
   adjudicated here. If substantive retained template expression is identified later,
   obtain permission or remove it before release; attribution alone is not permission.
4. **External dependencies:** Remotion/React/Pillow/Piper implementations, browser,
   voice weights, recordings and functional LinkedIn bundle are not vendored. Declaring
   or invoking dependencies differs from redistributing them. Remotion core/media use
   custom terms; the pinned media license classification is resolved. The Windows
   native bundle's FFmpeg is GPL-2.0-or-later, but complete executable/DLL redistribution
   mapping is still unverified. Optional Piper is GPL-3.0-or-later; no blanket subprocess
   exemption is asserted. Future binary/container bundles need their own notices,
   source-compliance and use-rights review. See [third-party review](THIRD_PARTY_NOTICES.md)
   and [dependency inventory](docs/dependency-licenses.json).

## Scoped licensing decision and remaining limitations

- The owner's explicit instruction establishes the chosen attribution and scoped MIT
  authorization for the original portions owned. It does not independently verify
  employer/contributor rights or make adapted renderer/instructions wholly independent.
  Any original/local portion outside that ownership still needs permission. Private
  possession, a fork and AI generation are not substitutes for such permission.
- The identified starter bootstrap/config replacement is implemented and tested as
  described above. Retain its historical attribution and requirements-based provenance.
  This removes the identified inherited implementation from the candidate; it does not
  certify copyrightability or erase obligations if protected expression is later found.
  Do not label this AI-assisted work a legally verified clean-room implementation.
- Keep the upstream MIT notice and separate Vera license. Permission to use MIT
  material does not permit erasing its notices or renaming its copyright holder.
  If more upstream prompts/code are included later, map them explicitly and carry
  their license, including modified versions. No currently verified third-party asset
  requires replacement merely because it is third-party; comply with its actual terms.
- MIT is selected and applied to the original portions within the rights held by
  Mitra Arian; Apache-2.0 is not applied. The standard LICENSE text is unmodified
  except for the explicitly confirmed year/name. Scope is documented in README.md
  and THIRD_PARTY_NOTICES.md rather than by inventing extra MIT license conditions.
- A new source-only MIT candidate ZIP contains exactly the final 29-file allowlist,
  including LICENSE, all font notices and upstream attribution. It was reopened and
  compared byte for byte to the source manifest, then scanned for private material.
  Older ZIPs remain unchanged historical snapshots and are not current release files.

## Prior functional validation and preservation

Fresh follow-up checks used a new isolated copy and new Python environment, with
no dependency installation or generated output in the clean public source folder:

- Fresh Pillow 13.0.0 install from official PyPI: pass.
- Locked `npm ci --offline --ignore-scripts --no-audit --no-fund`: pass, 186 packages.
  This is a clean installation from the existing npm cache, not a cold-cache test.
- `npm run check` and Node syntax check: pass.
- `python tests/smoke.py`: pass; seven ordered RGB 1080x1350 PNGs, absent internal
  header, measured bounds, public caption URLs, timing and negative-boundary checks.
- `python tests/smoke.py --video`: pass; actual 32.021s MP4, 1080x1920/30fps,
  H.264/yuv420p + AAC, full decode, 12 sample-timed cues and at most two subtitle
  lines. Scene audio correlations are at least 0.999031. It uses explicitly labeled
  **test tones, not narration**. Existing browser/FFmpeg were supplied externally.
- Both new seven-slide sets match prior validated PNG hashes byte for byte. The
  full MP4 also matches the previous fixture SHA-256:
  `77ea957c001638fb5ca684508e714d7ad7b15e8afb66f54210978bd3a3cc176e`.
  Assistant visual inspection of seven 360px slide previews and six MP4-derived
  scene previews found readable text/subtitles and no clipping. This is bounded
  visual self-review, not human listening or a claim that every frame was inspected.
- That scaffold follow-up left the composition, Python engine, Node renderer, tests,
  assets, skill, manifests and private-data exclusions byte-identical. The current
  license follow-up changes only documentation, root license metadata and the export
  allowlist (adding LICENSE). Dependency records/versions and production code are unchanged.
  All 755 baseline-protected original project/content/media/Git files still match.

## Final scoped-MIT privacy and packaging check

The final source tree and refreshed source-only ZIP contain exactly **29 files**.
Explicit allowlisting, secret/personal-path scans, 181 private topic/caption phrase
comparisons and archive CRC/SHA-256 byte comparisons pass. Personal posts, captions,
research, backlog/topic candidates, calendars, credentials, private paths, models,
recordings, generated media, dependencies/caches, Git history, symlinks and private
audit files are absent from both. Only the clearly synthetic demo (including its
fictional caption) and the separately licensed Vera fonts are intentionally included.
The copyright name explicitly authorized above is public attribution, not a leak.

The standard LICENSE text and the unchanged upstream MIT notice were checked;
font assets/notices and dependency inventory remain byte-identical. package.json
and package-lock.json agree on MIT for the original portions, and every non-root
lockfile record is unchanged. The export allowlist includes LICENSE. All 755
protected original files and all earlier archives remain unchanged.

Current changed public files: LICENSE (new), README.md, THIRD_PARTY_NOTICES.md,
RELEASE-READINESS.md, LICENSE-RECOMMENDATION.md, CONTRIBUTING.md, VALIDATION.md,
package.json, package-lock.json and scripts/audit_export.py (allowlist only).
Functional smoke tests described above remain applicable to unchanged production
code; they were not rerun for documentation/license metadata. Current packaging,
syntax, privacy and preservation checks were run on the final sources and archive.
Detailed manifests, checksums, authorization record and audit results stay outside
this source distribution. No original private project is modified or relicensed.

**Recommendation:** the scoped-MIT source-only package is technically ready for
local handoff. Do not present it as independently cleared ownership of all code;
resolve any rights outside the licensor's ownership before public release. No
repository creation, upload, commit, push, publication or paid service was used.
Remotion use eligibility, optional speech/output rights and the native package's
incomplete binary notice/build mapping remain separate limitations. No native
binary is bundled; this is not approval for a binary/container distribution.
Human listening was not repeated and fixture audio remains test tones, not speech.
