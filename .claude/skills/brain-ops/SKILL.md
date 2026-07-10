---
name: brain-ops
description: >-
  Core Brendan OS operations against the brendan_brain repo. Use whenever Brendan says
  things like "remember this", "add this to the Brain", "add to my research queue",
  "research this (now/tomorrow/deeply)", "make this a watch", "what does the Brain know
  about X", "what's in my queue", "what's waiting for me", or "system status". Also use
  to capture observations, preferences, decisions, and predictions during any conversation
  in a Brendan OS-enabled project.
---
<!-- brendan-os-skill-version: 1.0.0 (2026-07-10) — canonical source: brendan_brain/.claude/skills/brain-ops -->
# brain-ops

Locate the Brain: `../brendan_brain` from a specialist repo, or the current repo if it IS
brendan_brain. If absent, tell the user integration requires adding `brendan_brain` to this
session/routine's repository selection, and stop.

Before writing anything: read `CLAUDE.md` (contract) and, for anything sensitive,
`system/PRIVACY_POLICY.md`. Always `git pull --rebase origin main` first, and after
committing, push and verify with `git ls-remote origin main`.

## Commands

**capture / remember** — Classify per `system/MEMORY_POLICY.md` (casual mention → skip;
dated observation → timeline file; preference signal → PROPOSED_RULES evidence line;
decision/prediction → artifact; explicit "remember" → durable knowledge in the right
domain). Use SCHEMAS.md frontmatter. Preserve Brendan's wording; never upgrade an
observation into a diagnosis/fact.

**enqueue / research this** — Run:
`python3 tools/new_task.py --title "..." --domain <d> --request "<verbatim ask>" [flags]`
Map natural language to flags: "now"→`--urgency urgent`, "before tomorrow morning"→
`--deadline <tomorrow> --publish newspaper`, "quick answer"→`--depth quick`, "deep report"→
`--depth deep --effort until_strong`, "one research pass"→`--effort 1_pass`, "watch this"→
`--recurrence watch`, word counts→`--word-budget N`. If output starts with `DUPLICATE`,
tell Brendan it's already queued and note the +1 interest signal. Then ask any useful
intake questions IMMEDIATELY (classify blocking/material/optional per task schema); record
non-blocking assumptions in the task's `## Assumptions` and proceed.

**recall / what does the Brain know** — Run:
`python3 tools/brain_search.py "<terms>" [--domain d]`, open top hits, answer from
artifacts (cite ids). Sensitive artifacts need a matching --domain or --allow-sensitive
REASON (then log the reason in your output artifact).

**status / what's waiting for me** — Regenerate + read `QUEUE.md`
(`python3 tools/build_queue_dashboard.py`), list `waiting_for_brendan` tasks and open
questions in `newspaper/questions/`, and `python3 tools/oplog.py status` for unfinished
cross-repo operations.

**answer question** — Write the answer into the question artifact (`status: answered`) and
the owning task's `## Questions`; move the task out of `waiting_for_brendan` (git mv +
status update); resume or re-plan the task.

**propose rule / update preference** — Append evidence to `preferences/PROPOSED_RULES.md`.
Only Brendan's explicit instruction (or his approval of a proposal) touches
CONFIRMED_RULES.md.

After any writes: `python3 tools/validate_frontmatter.py --all && python3 tools/build_index.py
&& python3 tools/build_queue_dashboard.py`, commit with an area-prefixed message, push, verify.
