---
tags: [linux, filesystem, permissions]
---
The classes are owner, group and other. root overrides them through
`CAP_DAC_OVERRIDE`, even on a `0000` mode.

So "I want root to be able to read this" is never a question when choosing a
mode. What you are actually choosing is the right of the **owner**. A mode is a
policy for everybody except root, and restricting root itself needs a different
tool.

See [[Unix permissions]]
