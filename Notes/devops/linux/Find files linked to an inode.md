
To find files linked to an inode you can use the find comand : 

```bash
stat -c 'link=%h inode=%i' a.txt
find ~/lab -inum 8591547
```

```
link=3 inode=8591547
/home/ansible/lab/a.txt
/home/ansible/lab/b.txt
/home/ansible/lab/c.txt
```

## Cards
Q: how do you find every name pointing to a given inode?
A: `find <path> -inum <number>`.

Q: how do you read the reference count and the inode number of a file in one command?
A: `stat -c 'link=%h inode=%i' <file>`.
