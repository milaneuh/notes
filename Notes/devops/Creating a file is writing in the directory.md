When you create a file, you are writing in the directory. Not the file, which does not exist yet.

So the right you need is `w` on the **directory**, not on the file. This is why a permission error on file creation is always a question about the directory, and why the error message rarely says so.

Same thing for deletion: removing a file is a write to the directory, not to the file. You can delete a file you cannot read.

See [[Permissions on a directory]], [[umask]]

## Cards
Q: which permission do you need to create a file?
A: `w` on the **directory**, not on the file — the file does not exist yet, so you are writing in the directory.

Q: which permission do you need to delete a file?
A: `w` on the directory. Removing a file is a write to the directory, not to the file. You can delete a file you cannot read.

Q: a permission error on file creation is always a question about what?
A: the directory — and the error message rarely says so.
