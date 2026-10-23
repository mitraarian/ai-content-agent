# Local content production engine

Read `.agents/skills/content-production/SKILL.md` for weekly/monthly production.
Use `config.example.json` as the documented configuration contract. Keep personal
configuration, research, calendars, backlog and publishing assets in ignored
`content/`, `.local/` or `out/`; never add them to the distributable engine.
Use the configured optional writing guidance by reference, never copy private
profiles, story banks or plugin caches. Do not invent sources or personal results.
Default slide posts to ordered PNG images and a separate caption with public URLs.
Do not add internal project branding to slides. PDF is only an explicit opt-in.
There are no publishing, account or paid-service integrations in this engine.
Local production does not authorize remote actions, spending or publication.
Do not silently download models/browsers or substitute a narrator.
Run `npm run check` after TypeScript changes and `python tests/smoke.py` after
renderer changes. Inspect actual mobile previews and final video frames; state
which visual/listening checks were and were not performed.
