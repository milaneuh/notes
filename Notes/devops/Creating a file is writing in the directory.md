When you create a file, you are writing in the directory. Not the file, which does not exist yet.

So the right you need is `w` on the **directory**, not on the file. This is why a permission error on file creation is always a question about the directory, and why the error message rarely says so.

Same thing for deletion: removing a file is a write to the directory, not to the file. You can delete a file you cannot read.

See [[Permissions on a directory]], [[umask]]
