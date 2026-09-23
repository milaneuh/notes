A file is owned by the identity of the process that creates it, more precisely its effective UID. Not by whoever owns the directory.

So the data files of a service running as `svcuser` will always be owned by `svcuser`. They can not be owned by `root`, except if the service is ran as `root` but you should try to not do that usually.

This says nothing about the **directory** that contains them. A service directory can perfectly well be owned by `root`, as long as the service identity has `w` and `x` on it. That is often the better choice :

- `root:svcgroup 0770` the service writes inside, but can not `chmod` the directory to widen access, because that requires owning it
- `svcuser:svcgroup 0750` the service owns the directory, so a compromised service can widen it itself

Exception to remember : if the directory has the setgid bit, new entries inherit the group of the directory instead of the group of the process.

See [[Permissions on a directory]], [[root is not a permission class]], [[systemd StateDirectory]]

## Cards
Q: who owns a newly created file?
A: the identity of the process that created it, more precisely its effective UID. Not whoever owns the directory.

Q: why prefer `root:svcgroup 0770` over `svcuser:svcgroup 0750` for a service state directory?
A: the service can write inside but cannot `chmod` the directory to widen access, because that requires owning it. If the service owns it, a compromised service can widen it itself.

Q: what does the setgid bit on a directory change about ownership?
A: new entries inherit the group of the directory instead of the group of the creating process.

Q: can the data files of a service running as `svcuser` be owned by `root`?
A: no — they are owned by the effective UID of the process that writes them. Only the containing directory can be owned by root.
