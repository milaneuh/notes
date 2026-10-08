---
tags: [linux, tooling]
---
They answer different questions. [[df]] looks at a whole file system or
[[mount point]] and is instant, because it reads the block accounting. [[du]]
looks inside given directories and is slow, because it opens every file and
sub-directory.

They disagree for two reasons.

**A deleted file still held open.** df counts its blocks as used, du cannot see
a file that has no name any more. Find the holder with `lsof +L1`, free the
space by restarting the process.

**What they measure.** du reports apparent size or blocks used per file it
walks, df tracks the whole partition, so sparse files make the two diverge.
