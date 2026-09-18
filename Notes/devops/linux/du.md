The du (disk usage) command shows the disk usage within directories and files in the [[File System]]

Example : 
```bash
	du -h /home/example-directory
```

The -h options here is to display the size in a human readable format. 

Output :
```
44K /home/example-directory/data
2.0M /home/example-directory/main.go
10M /home/example-directory/test
```

See [[df vs du]]