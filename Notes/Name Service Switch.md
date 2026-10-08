---
tags: [networking, linux]
---
NSS connects the system to the databases that answer lookups, not only
hostnames but `passwd`, `group`, `shadow`, `services`. Each line of
`/etc/nsswitch.conf` names one database and its sources, in order:

```conf
passwd:     files ldap
hosts:      dns nis files
```

So the `hosts:` line decides whether `/etc/hosts` is consulted before DNS. The
order is declared, not universal: with `dns` first, a local entry is ignored
whenever an earlier source answers. Read the line instead of assuming.

See [[Name resolution]]
