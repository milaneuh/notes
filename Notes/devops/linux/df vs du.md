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