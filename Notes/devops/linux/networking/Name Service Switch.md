The Name Service Switch (NSS) is a feature that connects a computer with a variety of configuration databases and name resolution services.

## nsswitch.conf

To configure the [[linux]] name services you usually use this file. This file lists databases, and the sources used for name resolution. 

Example : 

```conf
passwd:     files ldap
shadow:     files
group:      files ldap

hosts:      dns nis files

ethers:     files nis
netmasks:   files nis
networks:   files nis
protocols:  files nis
rpc:        files nis
services:   files nis

automount:  files
aliases:    files
```

## Cards
Q: what does NSS do?
A: it connects the system to the databases that answer lookups, hostnames among others, but also passwd, group and shadow.

Q: what does one line of `/etc/nsswitch.conf` declare?
A: one database, then the sources consulted for it, in order.

Q: `hosts: dns nis files`, what does that order mean?
A: DNS is queried before `/etc/hosts`, so a local entry is ignored when an earlier source answers.
