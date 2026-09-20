sed is the default tool for text transformation in linux. 

sed is used with the `s` command :

```bash
s/PATTERN/REMPLACEMENT/FLAGS
```

- PATTERN is a regular expression 
- REMPLACEMENT is the remplacing text
- FLAGS g (global), i (case insecitive), 2 (second occurence only)  

Example : 

```bash
sed 's/prod/release/g' hosts.old
```

> Remplace every (g) 'prod' occurence in the text with 'release'

To directly write into the file, use the `-i`.
To delete the occurence you can use `d` : `s/prod/d`
To create group you can use `-E`
To automatically create a backup use `-i.bak`

Example of a complete workflow : 

```bash
# Make a backup copy
cp db.conf db.conf.orig

# Apply all the transformation in one go
sed -E -i.bak \
  -e 's/host[[:space:]]*=[[:space:]]*.*/host=db.staging.example.com/' \
  -e 's/database[[:space:]]*=[[:space:]]*.*/database=staging/' \
  -e 's/[[:space:]]*=[[:space:]]*/=/' \
  -e '/^#/d' \
  -e '/^$/d' \
  db.conf

# Verify the result 
cat db.conf

# Verify the difference with the backup file
diff db.conf.orig db.conf
```