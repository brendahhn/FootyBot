---
name: safe-bot-edits
description: >
  Use this skill whenever Brendan wants to change, extend, tune, or add to one of his
  autonomous "robots" — the Jobs Robot (repo: brendahhn/operator-notebook), the Health
  Research Robot (repo: brendahhn/health-notebook), or FootyBot (repo: brendahhn/footybot).
  Triggers on any request like "add more X to the bot", "broaden the search", "I want it to
  also do Y", "throw these topics in", "change how it Z", "tune the prompt", "stop showing me
  W", or any edit to a bot's operating prompt, notebook, or idea queue. These bots run
  unattended on a schedule with no human watching, so every change carries a specific failure
  mode this skill exists to prevent. Do NOT use this skill for ordinary coding tasks unrelated
  to these bots.
---

# Safe Bot Edits

Brendan has scheduled, unattended AI "robots." Each one's behavior is driven by a prompt
file in its repo, its memory is a notebook file, and topics it should work on later live in an
idea-queue file. Brendan edits these by describing what he wants in plain English in a Claude
Code session. Your job is to make that change **safely**, because a careless edit silently
changes what an unattended bot does at its next scheduled run, with no human watching to catch it.

This skill is the procedure. Follow it exactly. Brendan is non-technical about git — explain
what you're doing in plain English, and never make him answer a git question he can't answer.

## The bots and their files

| Bot | Repo | Prompt file (behavior) | Memory (brain) | Backlog (topics) |
|-----|------|------------------------|----------------|------------------|
| Jobs Robot | `brendahhn/operator-notebook` | `jobs-operating-prompt.md` | `jobs-notebook.md` | _(jobs queue if present)_ |
| Health Robot | `brendahhn/health-notebook` | `health-robot-prompt.md` | `health-notebook.md` | `idea-queue.md` |
| FootyBot | `brendahhn/footybot` | `footybot-operating-prompt.md` | `footybot-notebook.md` | `footybot-idea-queue.md` |

If you're unsure which repo you're in, run `git remote -v` and match it. Never edit the wrong bot.

## STEP 0 — Classify the request FIRST

Every request is one of two kinds. Decide which before doing anything, because they take
totally different paths:

- **TOPIC** — "research X", "look into Y", "add these subjects/companies/role-types to look at
  later", a raw dump of ideas. The bot should *work on this later*; it is not a behavior change.
  → Go to PATH A (queue). Do NOT touch the prompt.
- **BEHAVIOR** — "change how it works", "broaden/narrow the search", "stop doing Z", "add a new
  step", "tune the filters", "change my targets", "edit the prompt". The bot should *act
  differently every run*.
  → Go to PATH B (prompt edit).

If a request is genuinely both (e.g. "add these topics AND make it go deeper on everything"),
split it: do the topic part via PATH A and the behavior part via PATH B, separately, each fully.

When in doubt, ask Brendan one plain question: "Do you want the bot to *research this later*
(I'll add it to its list), or *behave differently every run* (I'll edit how it works)?"

---

## PATH A — TOPIC (dump into the queue)

Low-risk. The bot consumes these later; nothing about how it runs changes.

1. Find the bot's queue/backlog file (Health Robot: `idea-queue.md`; FootyBot:
   `footybot-idea-queue.md`; Jobs Robot: a queue file if one exists — if none exists, ask
   Brendan whether to create one or add the topics to the notebook's appropriate section).
2. Append the topics **verbatim** under the file's INBOX/unsorted section, as a dated dump.
   Do not sort, tag, research, or edit them — the bot does that on its own later. Do not touch
   any other file.
3. Commit only that file. Push. **Verify the push landed** (see SHARED RULES).
4. Tell Brendan what you added and that nothing happens to it until the bot reaches it in its
   normal cycle.

That's it. No diagnose step, no diff review needed for a pure topic dump — it's just adding
text to a list.

---

## PATH B — BEHAVIOR (edit the prompt) — the careful path

This changes what the unattended bot does every run. Four sub-steps, in order. Do not skip the
diagnosis.

### B1 — Diagnose BEFORE you change anything (read-only)
Do not jump straight to editing. First understand *why* the current behavior is what it is, so
the fix addresses the real cause instead of guessing. Read the prompt file and the notebook, and
look at recent run history. Then tell Brendan in plain English what's actually going on.

The classic example: "I'm only getting one job a day, broaden the search." Before widening
anything, check the notebook — is the bot *finding few roles* (then broadening helps), or
*finding many but cutting most at verification* (then broadening just produces more rejects and
won't fix it)? Same shape applies to the health bot. State the cause, then propose the fix.

### B2 — Propose the change and the tradeoff, get a nod
Tell Brendan specifically what lines/sections you'd change and what the tradeoff is. The most
common hidden trap: "broaden" can quietly become "lower the quality bar." Make the tradeoff
explicit — e.g. "I can add FP&A, RevOps, and AI-ops as target roles (more good volume), OR I can
loosen the verification filters (more volume but more dead/junk listings). I'd do the first, not
the second." Let him choose before you edit.

### B3 — Make the edit, preserving the rails
Edit only the prompt file. While editing, NEVER weaken these without Brendan explicitly asking:
- the verification bar (real PMID/DOI for health; live/verified posting for jobs — a broadened
  search must still cut dead/fake results)
- the provider-gating rule (health bot: it researches, never prescribes; flags dose/med/supplement
  changes as provider-gated)
- the critic/self-review pass
- the branch rule (read and write the same canonical branch every run, verify the push)
"Broaden coverage" is almost never a reason to touch any of those. If a request seems to require
weakening a rail, stop and flag it to Brendan rather than doing it silently.

### B4 — Finish safely
- Bump the version-date comment at the top of the prompt (add a short rev marker describing the
  change), so Brendan can tell which version ran on a given day.
- Confirm the file's final non-blank line is still exactly `## END`. This is a hard requirement:
  the bot's bootstrap refuses to run a prompt that doesn't end in `## END`, so if an edit drops
  it, the bot silently does nothing at its next run. Always re-check it after editing.
- Commit to the canonical branch, push, and **verify the push landed** (SHARED RULES).
- **Show Brendan a diff summary and STOP.** Do not move on. He reads the diff before trusting it.
  This is the single most important rail: twice, the real bug was not where anyone expected, and
  the ten-second diff read is what would have caught it. Present the diff plainly: what changed,
  what did NOT change, confirm `## END` intact, confirm the rails above untouched.

---

## SHARED RULES (apply on every path)

**The bot must never edit its own prompt unattended.** Prompt changes only happen here, in a
session with Brendan reading the diff. The scheduled bot edits its *notebook* (memory) every run —
that's normal and expected — but never its prompt. If asked to make the bot self-modify its
prompt, decline and explain why: it removes the human-reads-the-diff safety margin.

**Verify writes; never assume them.** After any commit+push, run `git ls-remote origin <branch>`
and confirm the new commit hash actually appears on the branch you think you pushed to. The whole
memory loop depends on reading and writing the *same* branch every run. (History: one bot spent
8 runs silently writing to a side branch because a push to `main` was being blocked and falling
back without anyone noticing. Verifying the push is what prevents that class of bug.)

**Branch reality is per-environment — check, don't assume.** If a push is ever rejected (e.g. 403)
or lands somewhere unexpected, do NOT silently scatter to a new side branch. Tell Brendan the
exact branch it actually used, and pin that reachable branch as canonical so reads and writes
match. Both bots currently push to `main` cleanly from the scheduled routine; a chat session may
start on a throwaway `claude/*` branch, which only affects pushes made from the session, not the
routine.

**One bot at a time, one change at a time.** If editing the same step/section twice in a session,
do the edits sequentially and re-read the file between them so the second edit doesn't step on the
first. Confirm each lands before the next.

**Plain English always.** Brendan is non-technical about git. Explain what you're doing and why,
in plain terms. Never end a turn by asking him a git question he can't answer — diagnose it
yourself (read-only) and report what you found.

**The browser step is his, and it's separate.** Each bot's routine *config* (in the browser) holds
a thin bootstrap pointer; the real instructions live in the prompt file you edit. Editing the file
is enough for the scheduled bot to pick up the change next run — he does NOT need to touch the
browser for a normal edit. Only remind him about the browser config if the bootstrap itself needs
changing (rare).
