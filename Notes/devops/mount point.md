On [[linux]] systems you do not have drive letters (like C:/ on windows). Instead, everything gets attached at some directory ([[mount point]]). So any path underneath it is served from there. 

Not every directory is a mount point however, they are just folders living under inside whatever filesystem is mounted on `/` unless the path is itself a mount point (nearest mount point above the path wins). Usually you only have a handfull of mount on the top level directory. `/etc` , `/usr`, `var` are _often_ simple directories, not separate attachment.

