# Proposed prompt change — Brain integration (NOT applied)

Per safe-bot-edits, `footybot-operating-prompt.md` is only edited in a Brendan-reviewed session. Exact proposed
diff — two additive lines, no existing behavior changed:

Add immediately after the existing memory-READ step:

```
STEP (Brain read, optional — only if ../brendan_brain exists): Follow the READ section of
.claude/skills/brain-sync/SKILL.md. If absent, note "brain-sync: skipped" in the changelog.
```

Add immediately after the existing memory-WRITE step:

```
STEP (Brain write, optional — only if ../brendan_brain exists): Follow the WRITE section of
.claude/skills/brain-sync/SKILL.md. Brain push failure never blocks this run; log it.
```

Bump the version-date comment at the top; keep `## END` as the final line. Rollback:
delete the two lines — the "only if" guards make absence a no-op.
