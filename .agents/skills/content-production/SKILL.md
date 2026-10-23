---
name: content-production
description: Prepare local weekly or monthly educational content packages from a configurable brief, including ordered LinkedIn PNG slides and narrated Remotion MP4s. Use for content-package production, research, rendering and QC; no automatic publishing.
---

# Content production

Read project AGENTS.md, README.md and the chosen configuration first. Resolve paths
from the project root, not a machine-specific workspace. Use the existing renderer
and editable example schemas; do not introduce an app or a competing framework.

1. Establish the audience, language, platform, timezone and proposed cadence from
   the configuration/user brief. The cadence is an editorial proposal, never an
   instruction to schedule social posts. English LTR LinkedIn assets are implemented;
   Persian RTL/Instagram adaptations require separately implemented and validated
   typography, narration and platform layout. Do not imply they already work.
2. Read the local private `content/topic-backlog.md` before new weekly/monthly research.
   Compare angles against Scheduled and Published topics and linked calendars.
   Never copy another installation's topics. Create an empty backlog only when
   absent, with Candidate, Selected, Scheduled and Published states. Scheduled means
   assigned to an editorial calendar; Published requires explicit confirmation.
3. For each monthly batch, investigate recent educational AI/software content on
   YouTube, LinkedIn and Instagram. Save a dated private `topic-research.md` containing
   searches/recency window, real item URLs, topic, date, visible engagement and
   observation date, audience pain point, brief hook paraphrase and format. Mark
   unknown/blocked fields, document access attempts and continue with accessible
   evidence. Never invent metrics, equate counts across platforms or bypass access
   controls. Compare recurring themes across all three platforms with evidence gaps.
   Use Hacker News, Reddit, GitHub, primary docs and papers for depth and verification.
4. Rank original topic candidates by audience interest 30%, educational depth 30%,
   technical relevance 20%, freshness/visual storytelling 20%. Retain sources and
   selection rationale. Update the local backlog after planning; preserve historical
   research. Reuse optional separately installed LinkedIn planner, writer, humanizer
   and repurposer guidance when available. Read their instructions; disregard
   unverified reach claims and any default auto-publishing action.
5. Start each explanation with a concrete example. Define unfamiliar terms and
   distinguish sourced facts, analysis and explicitly hypothetical examples. Map
   material claims to primary URLs, sections, dates and caveats in sources.md.
   Compare evidence with the exact claim; remove unsupported statements. Write
   original wording/visuals, never copy creators' scripts or personal stories.
6. Create date-specific ignored content folders containing editable JSON, plan,
   hooks, source/claim map, caption.md with public URLs, review and validation notes.
   Preserve approved assets; use new revisions rather than overwrite them. Fill the
   example schema with original content; the synthetic demo is not a topic backlog.
7. Render 6-8 ordered RGB PNGs (default 1080x1350), cover and 360px mobile previews.
   Keep section titles and slide numbers; no internal project header. PDF is optional
   only when explicitly requested (`slides --pdf`). Validate order, dimensions and
   measured bounds; visually inspect final images at mobile size.
8. For video, create 5-7 short scenes and phrase-level narration. Explicitly select
   an authorized optional Piper voice or supply one mono PCM WAV per phrase.
   `prepare-video` measures the audio samples and generates scene timing, joined
   narration and SRT; `render-video` burns captions into the Remotion MP4. Check
   30-60 seconds, audio/video tracks, synchronization, two subtitle lines and readable
   safe areas. Listen for pronunciation and cut-offs; never label fixture tones speech.
9. Produce calendar and upload instructions linking local final assets in order.
   Record exact checks, blockers, voice rights and human review still needed. No
   source verification or naturalness claim may be based solely on self-scoring.
   Continue unaffected posts if one item fails. Stop before publishing, scheduling,
   account connections, paid services or downloads not authorized by the user.
