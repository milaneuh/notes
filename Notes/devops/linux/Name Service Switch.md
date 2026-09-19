The Name Service Switch (NSS) is a feature that connects a computer with a variety of configuration databases and name resolution services.

## nsswitch.conf

To configure the [[linux]] name services you usually use this file. This file will lists databases, and other sources for obtaining the name resolution. 

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

