On a **directory**, the three rights do not mean what they mean on a file :
1. `r` list the names in the directory
2. `w` create or delete entries in the directory
3. `x` traverse the directory, ie. resolve a name inside it

`x` is the gate. Without it nothing inside is reachable by path, whatever the mode of the files themselves. With `r` but no `x` you can list the names but not open them.

So when you are configuring the permissions of a directory, remember that the non null number should always be impair (because `x` is 1). The usual directory modes are `0700`, `0750`, `0755`, `0770`, `0775`. It is rare to see permissions like `0660` since it means you can not traverse the directory, so it is almost always a bug.

On a **file** the same letters mean : `r` read the content, `w` modify it, `x` execute it as a program. The `x` bit on a data file is meaningless.

To close access to the content of a directory, remove `x` from `other` on the directory. That is more effective than tightening each file inside.

See [[Creating a file is writing in the directory]], [[umask]]
