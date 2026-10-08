---
tags: [linux]
---
A fixed-size circular memory area holding the kernel's log messages. New
messages overwrite the oldest, so an old event can simply be gone.

It holds what no user-space log can: boot events, device drivers and hardware
warnings, recorded before user-space logging exists.

Read it with [[dmesg]].
