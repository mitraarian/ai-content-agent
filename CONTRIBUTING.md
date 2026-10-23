# Contributing

Keep the engine small and data-driven. Reuse the existing slide layout and Remotion
primitives; no web application, new agent hierarchy or automatic account actions.
Use synthetic examples only. Keep private briefs, calendars, research, analytics,
voice models and generated exports outside the distributable source tree.

Run `npm run check` and `python tests/smoke.py`. Renderer changes require final
mobile preview inspection; motion/audio changes also require the optional full
video smoke test and listening review. Record what was actually tested. Do not
turn a fixture tone into a claim of working speech. Never invent source/performance
metrics. Review dependency licenses before updates; keep Remotion packages aligned.

Before contributing code, confirm you own it or can contribute it under the MIT
license in LICENSE; preserve applicable third-party notices. The project MIT scope
covers only rights actually held. There is no contribution license agreement or
assumption of ownership transfer.
Do not send secrets, private stories or generated personal content in issues/patches.
