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

## Cards
Q: what does umask do to a requested mode?
A: it subtracts. The result is `requested mode AND NOT umask` — it never adds a bit the program did not ask for in the first place.

Q: how do you write a umask from scratch?
A: answer "what do I forbid here?" three times, with `r=4 w=2 x=1`. Forbid nothing for owner, write for group, everything for other -> `027`.

Q: why can you not predict a file mode from the umask alone?
A: because the result depends on what the program requests. Most programs ask `0666` for files and `0777` for directories, SQLite asks `0644`, key tools ask `0600`.

Q: umask 027 — what mode does a file get, and a directory?
A: `0640` for a file (from 0666), `0750` for a directory (from 0777).

Q: umask 077 — what mode does a file get, and a directory?
A: `0600` for a file, `0700` for a directory. Owner only.

Q: why is "the mask is 7 minus what I want" wrong?
A: it only works for directories, because they are the thing requested at `0777`. For files the request is `0666`, so the arithmetic breaks. Check with `ls -l` instead of trusting it.
