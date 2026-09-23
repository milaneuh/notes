An hardlink add an entry in a **directory** to an existing [[inode]], it does not copy anything. 

Example : 

```bash
echo "original content" > report.txt
ln report.txt report-copy.txt
ls -li report.txt report-copy.txt
```

```
8591538 -rw-r--r--. 2 ansible ansible 17 Jul 23 10:04 report-copy.txt
8591538 -rw-r--r--. 2 ansible ansible 17 Jul 23 10:04 report.txt
```

We can observe here that the inode identifier is the same between the two files, and the count went from 1 to 2 because two files are linked to that inode. 

That implies that if we modify one of the files, the second should be updated as well : 

```bash
echo "new line" >> report-copy.txt
cat report.txt
```

```
original content
new line
```

And deleting one file does not delete the inode while another file is referencing it :

```bash
rm report.txt
ls -li report-copy.txt
cat report-copy.txt
```

```
8591538 -rw-r--r--. 1 ansible ansible 26 Jul 23 10:05 report-copy.txt
original content
new line
```

The count number went back to one, since one reference to the inode was deleted

See 
- [[Find files linked to an inode]]
- [[hardlink limits]]
- [[a file is not it's name]]

## Cards
Q: what does a hardlink do?
A: it adds an entry in a directory pointing to an existing inode. It copies nothing.

Q: you hardlink a file. What happens to the inode number and to the reference counter?
A: both names share the same inode number, and the counter goes from 1 to 2.

Q: you modify a file through one of its hardlinks. What does the other name show?
A: the same new content. There is only one file, with two names.

Q: you delete one of two hardlinks. What happens to the content?
A: nothing, it is still there under the remaining name. Only the counter goes back to 1, because one reference to the inode was removed.
