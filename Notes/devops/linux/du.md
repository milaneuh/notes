The du (disk usage) command shows the disk usage within directories and files in the [[File System]]

Example : 
```bash
	du -ah /home/example-directory
```

The -h options here is to display the size in a human readable format. The `-a` is what makes it list the **files** too : without it, du only reports directories. 

Output :
```
44K /home/example-directory/data
2.0M /home/example-directory/main.go
10M /home/example-directory/test
```

See [[df vs du]]

## Cards
Q: what does du show?
A: the disk usage of the directories and files inside a path, by walking the tree one entry at a time.

Q: `du -h` on a directory does not list the files inside it. Why?
A: without `-a`, du only reports directories. `-a` is what makes it list the files too.
