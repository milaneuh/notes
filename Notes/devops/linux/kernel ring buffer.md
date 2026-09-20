The kernel ring buffer is a fixed-size memory area that stores the [[linux]] system log messages.

It uses a circular design, meaning any new message will overwrite the oldest ones when the memory is full. It captures boot events, device drivers, and hardware warnings before user-space logging starts.

## Cards
Q: what happens to the oldest messages in the kernel ring buffer?
A: they are overwritten. The buffer is a fixed size and circular, so an old event can simply be gone.

Q: what does it hold that a user-space log cannot?
A: boot events, device drivers and hardware warnings, recorded before user-space logging exists.
