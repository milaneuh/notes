the kernel ring buffer is a fixed-size memory area that stores the [[linux]] system log messages.

it uses a circular design, meaning any new message will override the oldest ones when the memory is full. It captures boot events, device drivers, and hardware warnings before user-space logging starts.