StateDirectory is an option for [[systemd]] services, this option takes as a input a whitespaced-sperated list of directory names.

When the unit is started, the directories defined by the specified names will be created below `/var/lib`, also, the environment variable `$STATE_DIRECTORY` will be defined with the full path of the directories. 

Unless an User or a Group is specified, the directory will be owned by root. 

Example :

```bash
StateDirectory=aaa/bbb ccc
```
Then the `$STATE_DIRECTORY` variable will be set to "/var/lib/aaa/bbb:/var/lib/ccc"

`StateDirectory` takes over an **existing** directory too : it rewrites its owner and its mode at every start. So any `chown` or `chmod` you did by hand on that directory is silently reverted the next time the service starts.

`StateDirectoryMode=` defaults to `0755`, which means `other` can still traverse and list the directory. Set it explicitly if you do not want that, `0750` gives the owner everything and the group read and traverse.

It only controls the **directory**. The mode of the files created inside comes from the [[umask]] of the process, so you need `UMask=` in the same unit to control those.

```bash
StateDirectory=catalog-api
StateDirectoryMode=0750
UMask=027
```

If you need an owner that systemd would not choose, for instance keeping the directory owned by `root` while the service writes inside it, `StateDirectory` cannot do it. Declare the directory in a file under `/etc/tmpfiles.d/` instead, see `man tmpfiles.d`.

The reason to use any of this : the fix lives in a versioned unit file instead of a `chmod` somebody typed once. See [[File ownership]].
