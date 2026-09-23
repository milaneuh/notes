The disk free [[df]] command and the disk usage [[du]] command are often confused together. 
Even though both command allows us to see sizes in system or files, they are not aimed for the same use case, as their name implies.

Here lies the key differences : 

- Scope 
	- df looks at the whole [[File System]] or [[mount point]]
	- du looks inside specific folders or files
- Speed
	- df is very fast because it reads file system block allocation tables
	- du is slower because it scans every file and sub-folder one by one
- Why results can differ : 
	- If a running process holds onto a deleted file, df will show the space as used, but du will not see that file and will report smaller usage, as seen here : [[Diagnosing a systemd service]]
	- du reports the apparent file size or actual space used per block, whereas df tracks overall partition blocks

## Cards
Q: df and du, which one looks at what?
A: df looks at the whole file system or mount point, du looks inside specific folders or files.

Q: why is df fast and du slow?
A: df reads the file system's block accounting, du scans every file and sub-folder one by one.

Q: df says the file system is full, du reports far less usage. What is happening?
A: a running process holds a deleted file open. df counts the blocks as used, du cannot see a file that has no name any more.

Q: name a second reason df and du can disagree.
A: du reports the apparent file size or the actual space used per block of what it walks, while df tracks the overall partition blocks. Sparse files make the two diverge.
