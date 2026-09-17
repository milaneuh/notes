On [[linux]] systems you do not have drive letters (like C:/ on windows). Instead, everything gets attached at some directory ([[mount point]]). So any path underneath it is served from there. 

Not every directory is a mount point however, they are just folders living under inside whatever filesystem is mounted on `/` unless the path is itself a mount point (nearest mount point above the path wins). Usually you only have a handfull of mount on the top level directory. `/etc` , `/usr`, `var` are _often_ simple directories, not separate attachment.


## Cards
Q: linux has no drive letters — what does it use instead?
A: mount points. Every filesystem gets attached at some directory, and any path underneath it is served from there.

Q: if a path is not itself a mount point, which filesystem serves it?
A: the nearest mount point above it wins.

Q: are `/etc`, `/usr`, `/var` mount points?
A: usually not — they are often simple directories living inside whatever filesystem is mounted on `/`. Typically only a handful of top-level directories are real attachments.
