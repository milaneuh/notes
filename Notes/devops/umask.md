`umask` is the *user file-creation mode mask*. The digits are the permissions you are `removing` from the class, not the permissions you are `giving` it.

You write it by answering three times "what do I forbid here ?", with `r=4 w=2 x=1` :

```
owner : forbid nothing      -> 0
group : forbid write        -> 2
other : forbid everything   -> 7
                               umask 027
```

A umask can only **subtract**. It never adds a bit that was not requested in the first place.

The result is `requested mode AND NOT umask`, so you can not reason about it without knowing what the program asks for :

```
most programs   0666 for files, 0777 for directories
SQLite          0644
key tools       0600

0644 requested & ~0027  ->  0640
```

The four masks worth memorising :

| umask | meaning                     | file from 0666 | dir from 0777 |
| ----- | --------------------------- | -------------- | ------------- |
| 022   | the default, everyone reads | 0644           | 0755          |
| 027   | group reads, other nothing  | 0640           | 0750          |
| 007   | group reads and writes      | 0660           | 0770          |
| 077   | owner only                  | 0600           | 0700          |

Trap : "the mask is 7 minus what I want" is wrong. It only works for directories, because they are requested at `0777`.

Always check the result with `ls -l` instead of trusting the arithmetic, because the requested mode is a property of the program, not of the system.

See [[Permissions on a directory]], [[systemd StateDirectory]]
