# Third-party notices and review

Reviewed against installed metadata and primary upstream sources during preparation.
This file distinguishes included assets from separately installed dependencies;
release-owner review of complete transitive notices remains necessary.

The root [MIT LICENSE](LICENSE), Copyright (c) 2026 Mitra Arian, applies only to
original project code/documentation to the extent Mitra Arian owns those rights.
That attribution and scope were explicitly approved by the project owner; no
ownership of third-party material is implied or transferred. Preserve every
separate notice below, including Sergey Bulaev's complete upstream MIT notice
and public/fonts/bitstream-vera-license.txt. Root/package MIT metadata does not
relicense fonts, Remotion, FFmpeg, optional Piper or other dependencies.


| Component | Status and terms | Source / action |
|---|---|---|
| Vera.ttf, VeraBd.ttf | Included unmodified; Bitstream Vera font license permits bundling with notices, no standalone font sale and naming restrictions for modifications | Complete notice in public/fonts/bitstream-vera-license.txt; [upstream license](https://raw.githubusercontent.com/MrBitBucket/reportlab-mirror/master/src/reportlab/fonts/bitstream-vera-license.txt) |
| Pillow 13.0.0 | External Python dependency, MIT-CMU; native wheel components may have additional notices | [exact license](https://github.com/python-pillow/Pillow/blob/13.0.0/LICENSE) |
| Remotion core/bundler/renderer and @remotion/media 4.0.537 | External dependencies; custom Remotion free/company license, not MIT | [license](https://github.com/remotion-dev/remotion/blob/v4.0.537/LICENSE.md); verify pinned release terms; no license purchase is automated |
| React / React DOM 19.2.3 | External dependencies, MIT | [React license](https://github.com/facebook/react/blob/main/LICENSE) |
| TypeScript 5.9.3 | External development dependency, Apache-2.0 | [license](https://github.com/microsoft/TypeScript/blob/main/LICENSE.txt) |
| @types/react | External development dependency, MIT | Retain installed package notice |
| Piper 1.8.0 | Optional external process, GPL-3.0-or-later; not imported/bundled in core engine | [upstream](https://github.com/OHF-Voice/piper1-gpl), [version metadata](https://pypi.org/project/piper-tts/1.8.0/); review GPL/distribution boundary rather than assuming MIT |
| TTS voices / datasets / recordings | Not included; licenses, speaker and output rights are model-specific | Review each exact model card and original dataset. No narrator is mandatory/default |
| FFmpeg / libx264 / AAC | Not included; exact build matters: FFmpeg LGPL/GPL components and possible codec patent obligations | [FFmpeg legal](https://ffmpeg.org/legal.html); select and review your installation |
| Chrome / Chromium | Not included; executable supplied by user | Review browser and third-party notices of your installation |
| linkedin-skills | Optional separate checkout, observed MIT with copyright notice; no skill text/cache/profile/data redistributed | [repository](https://github.com/sergebulaev/linkedin-skills), [license](https://github.com/sergebulaev/linkedin-skills/blob/main/LICENSE) |
| ReportLab / PyMuPDF / pypdf | Not engine dependencies. PNGs render directly with Pillow; only unmodified, independently licensed Vera font assets were sourced from a ReportLab installation | PyMuPDF's [AGPL/commercial terms](https://pymupdf.readthedocs.io/en/latest/about.html) are not silently inherited into a supposedly permissive raster path |
| Stock media / music / original recordings | None included | Geometry is drawn locally; demo is fictional |

Do not copy dependency binaries, browser caches or voice weights into the repository.
Reusing an external speech process is an architectural choice, not a legal conclusion
that all GPL obligations vanish. The final distributor must review their actual use.
The installed lockfile inventory covers 186 packages: MIT, MPL-2.0, BSD,
Apache-2.0, ISC, CC-BY-4.0, Unlicense, 0BSD and Remotion/custom declarations.
See docs/dependency-licenses.json for observed package metadata and separate
upstream_review findings. The two exact gaps are:

- **@remotion/media@4.0.537 - license classification resolved.** The official npm
  artifact omits both license metadata and a notice. Its [version-pinned docs](https://github.com/remotion-dev/remotion/blob/v4.0.537/packages/docs/docs/media/index.mdx)
  explicitly identify the [Remotion License](https://github.com/remotion-dev/remotion/blob/v4.0.537/LICENSE.md).
  It is custom-licensed, not MIT. Our review does not pretend to amend npm metadata.
- **@remotion/compositor-win32-x64-msvc@4.0.537 - partial resolution.** The exact
  published artifact also has no license field or notice. [Official acknowledgements](https://www.remotion.dev/docs/acknowledgements)
  identify Remotion's FFmpeg distribution as GPLv2+; the matching Windows binary's
  `-L` output confirms GPL-2.0-or-later and its build enables GPL components.
  The [FFmpeg build repository license](https://github.com/remotion-dev/rust-ffmpeg-splitter/blob/main/LICENSE)
  agrees. This does not establish a single license for every native executable/DLL.
  Complete package notices and corresponding-source/build mapping remain unverified.
  Do not redistribute these binaries on the strength of this audit alone.

Both tarball integrity values were checked against the official npm registry and
our lockfile; neither contained a license/notice file. No native binary or runtime dependency
implementation is vendored in the clean source candidate; the historical starter
lineage and subsequent bootstrap/config replacement are assessed separately below.
Merely declaring dependencies
is distinct from redistributing their code. `npm ci`, however, installs platform
native packages including FFmpeg even with `--ignore-scripts`; recipients must
observe those packages' terms. A later binary/container/application bundle would
need its own licenses, notices, source-compliance and intended-use review.
Platform-specific packages not exercised here were not independently cleared.

The pinned lockfile is a dependency inventory, not a security or legal certification.
See LICENSE-RECOMMENDATION.md for the scoped MIT decision and remaining rights limits.

## Original-code and optional-integration boundaries

The original private source project's metadata was UNLICENSED. For this public
candidate, Mitra Arian explicitly approved MIT for the original code/documentation
only to the extent of rights held and supplied the 2026 attribution in LICENSE.
That resolves the license choice, not every possible contributor/employer claim.
No independent ownership clearance is asserted. No third-party rights or codec
patents are granted by the project's MIT notice.

Vera Regular/Bold and the complete notice were byte-matched to the referenced
upstream files. They may be bundled under their own font license with its notice;
keep those terms separate from the original portions' MIT license.

Piper is invoked through a separate CLI process with text/WAV interfaces. No Piper
source, runtime, voice or recording is distributed here. Its exact [1.8.0 license](https://github.com/OHF-Voice/piper1-gpl/blob/v1.8.0/COPYING)
and [package metadata](https://pypi.org/project/piper-tts/1.8.0/) establish
GPL-3.0-or-later. Calling a separately installed tool is not itself redistribution
of it; a combined distribution/integration needs its own copyleft analysis.
No blanket conclusion that subprocess use removes GPL obligations is intended.

The functional LinkedIn skill bundle, API clients, hook catalogs and media assets
are not vendored here. The local production brief used its guidance, and the public
production instructions adapt that brief. No substantive upstream verbatim prompt
body was detected, but that does not prove independence of modified instructions.
The notice below is retained conservatively for any protectable upstream guidance
adapted through that chain. This is not a finding that all new engine code belongs
to the upstream author or that all local additions have upstream MIT permission.
Private profiles and plugin caches remain excluded. Voice/dataset/output rights
are separate and no voice is selected by default.

## LinkedIn guidance provenance and retained MIT notice

Verified upstream: [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills),
commit `261240ac5c4da8b4465cbd364d14ce52ffed12ce`, release v1.1.23.
[License at that commit](https://github.com/sergebulaev/linkedin-skills/blob/261240ac5c4da8b4465cbd364d14ce52ffed12ce/LICENSE).
Keep this copyright and permission notice with copied or substantially adapted
upstream material, including prompts/instructions. A fork, reformatting or an
AI-assisted rewrite does not itself remove applicable obligations. This notice
licenses the upstream material on its terms; it does not transfer its ownership
to Mitra Arian. The separate root LICENSE covers only the original portions above.

```text
MIT License

Copyright (c) 2026 Sergey Bulaev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Remotion starter provenance and minimal replacement

Historical attribution: the studio's original index, Root, empty Composition and
TypeScript configuration match
[remotion-dev/template-empty](https://github.com/remotion-dev/template-empty/tree/bad1be9984b08a9ee3f3eee1df98765caa04ca11)
after line-ending normalization. The public candidate previously retained adapted
index/config fragments. The template's
[package metadata](https://github.com/remotion-dev/template-empty/blob/bad1be9984b08a9ee3f3eee1df98765caa04ca11/package.json)
says UNLICENSED, with no standalone LICENSE/LICENSE.md found; its README points to
Remotion's terms. This acknowledgement is not a permissive license grant.
The template's empty scene, logo and README body were never included here.

The inherited bootstrap/config implementation is now superseded. A new minimal
entry adapter constructs the unchanged local Root as a React element inside a
registered catalog component. It follows the
[Remotion registration contract](https://www.remotion.dev/docs/register-root) and
[React element API](https://react.dev/reference/react/createElement); it does not
copy a different template or merely rename the old bootstrap. The compiler settings
were rebuilt from the actual no-emit browser/React type-checking requirements,
using [TypeScript's bundler module guidance](https://www.typescriptlang.org/tsconfig/module.html)
and an explicit entry/import graph. Shared API names/imports and functional option
values remain unavoidable or appropriate; textual dissimilarity is not a rights test.
Manifest dependency/version/Node compatibility facts retain their acknowledged history
and are unchanged. The local visual engine, design, tests and fonts are unchanged.

A functional specification and before/after evidence were recorded privately before
implementation. This AI-assisted replacement was made after the prior code was seen;
it is not a clean-room certification, proof of copyrightability or blanket legal
clearance. Attribution or an AI rewrite alone does not remove third-party obligations.
If protected retained expression is subsequently identified, resolve its permission
or remove it before release. Historical attribution is deliberately preserved here.

Remotion remains an external npm dependency under its
[own pinned license](https://github.com/remotion-dev/remotion/blob/v4.0.537/LICENSE.md).
No Remotion SDK implementation or native dependency binaries are bundled in this
source candidate. Fresh locked install, TypeScript, seven-slide PNG and full fixture
MP4 smoke tests pass; see VALIDATION.md. Installing dependencies for local tests is
separate from redistributing them. The new 29-file source-only MIT candidate ZIP
includes this replacement and LICENSE; older ZIPs are retained historical snapshots
and must not be represented as the updated candidate.

The scoped project-license decision is resolved. Rights in any original/local
contributions outside Mitra Arian's ownership remain unconfirmed and are not granted
by this notice. The native package's incomplete binary notice/source mapping remains
a limitation for future binary redistribution; those binaries are absent here.
Remotion eligibility and optional speech/model/output rights require their own use
review. No publication is authorized and no blanket legal clearance is asserted.
