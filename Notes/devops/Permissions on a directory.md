On a **directory**, the three rights do not mean what they mean on a file :
1. `r` list the names in the directory
2. `w` create or delete entries in the directory
3. `x` traverse the directory, ie. resolve a name inside it

`x` is the gate. Without it nothing inside is reachable by path, whatever the mode of the files themselves. With `r` but no `x` you can list the names but not open them.

So when you are configuring the permissions of a directory, remember that the non null number should always be impair (because `x` is 1). The usual directory modes are `0700`, `0750`, `0755`, `0770`, `0775`. It is rare to see permissions like `0660` since it means you can not traverse the directory, so it is almost always a bug.

On a **file** the same letters mean : `r` read the content, `w` modify it, `x` execute it as a program. The `x` bit on a data file is meaningless.

To close access to the content of a directory, remove `x` from `other` on the directory. That is more effective than tightening each file inside.

See [[Creating a file is writing in the directory]], [[umask]]

## Cards
Q: on a directory, what does `r` mean?
A: list the names in the directory. Not open them — that needs `x`.

Q: on a directory, what does `w` mean?
A: create or delete entries in the directory.

Q: on a directory, what does `x` mean?
A: traverse it, ie. resolve a name inside it. It is the gate: without `x` nothing inside is reachable by path, whatever the mode of the files themselves.

Q: why should the non-null digits of a directory mode almost always be odd?
A: because `x` is 1, and without `x` the directory cannot be traversed. A mode like `0660` on a directory is almost always a bug.

Q: what is the effective way to close access to the content of a directory?
A: remove `x` from `other` on the directory. More effective than tightening each file inside.

Q: what does the `x` bit mean on a data file?
A: nothing useful — it means execute it as a program. On a data file it is meaningless.
