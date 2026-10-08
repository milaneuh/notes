---
tags: [linux]
---
The kernel cap on the length of an argument list, readable with
`getconf ARG_MAX`. Exceed it and the exec fails with `Argument list too long`,
which is why `cmd *` dies on a big directory where [[xargs]] or
`find -exec {} +` succeed.
