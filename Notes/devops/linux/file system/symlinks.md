A symbolic link (symlink), is it's own file, with it's own inode and the content of the file is simply a path reference. 

Example : 

```bash
echo "data" > target.txt
ln -s target.txt shortcut.txt
ls -li target.txt shortcut.txt
```

```
8591540 -rw-r--r--. 1 ansible ansible 8 Jul 23 10:04 target.txt
8591541 lrwxrwxrwx. 1 ansible ansible 9 Jul 23 10:04 shortcut.txt -> target.txt
```

This differ from [[hardlink]], the [[inode]] identifiers are different (8591540 & 8591541), the file type of shortcut is `l`.

symlinks bypass [[hardlink limits|the two limits of hardlinks]], which is why they are used more often.

## broken links
since symlinks only old paths to the reference link, nothing garanties that the path exists. If we delete `target.txt` the link will become a dangling link : 

```bash
rm target.txt
ls -l shortcut.txt
cat shortcut.txt
```

```
lrwxrwxrwx. 1 ansible ansible 9 Jul 23 10:04 shortcut.txt -> target.txt
cat: shortcut.txt: No such file or directory
```

The link still exists, we can still see it with `ls` but it is not linking anything. 

See 
- [[a file is not it's name]]

## Cards
Q: what is a symbolic link?
A: its own file, with its own inode, whose content is simply a path reference.

Q: in `ls -li`, how do you tell a symlink from a hardlink?
A: a symlink has a different inode number from its target, and its file type is `l`. A hardlink shares the inode number.

Q: what is a dangling link?
A: a symlink whose target path does not exist any more. `ls` still shows the link, but reading it fails with "No such file or directory".

Q: why are symlinks used more often than hardlinks?
A: because they bypass the two limits of hardlinks : they can point to a directory, and they can cross file systems.
