---
tags: [linux]
---
A configuration file on disk and the process that is supposed to obey it are
two different sources of truth. They agree only after a reload that actually
succeeded, and everything in between is where a diagnosis goes wrong: the file
says what you meant, the service does what it was last told.

Twice, in two domains. On a unit file I had written myself, `cat` showed a
clean unit while `systemctl cat` and `systemctl show -p` showed a `TasksMax=1`
coming from a drop-in I had never opened. On bind9, `named-checkconf -z`
reported the zone loaded while `dig @127.0.0.1` answered `NXDOMAIN`: the
validator reads the file, `dig` asks the process, and the server had not
reloaded.

**Validate the file, reload the service, then interrogate the service.**
Skipping the third step produces the false feeling of having applied something.
Worst case is a reload on a broken configuration: the previous one stays in
place, nothing visibly fails and nothing has changed.

Validators, before every reload: `sshd -t`, `named-checkconf -z`,
`named-checkzone`, `nginx -t`.

Effective state rather than intention: `systemctl cat`, `systemctl show -p`,
`nginx -T`, `named-compilezone`, and asking the service itself with `dig`,
`curl` or `ss`, which is the only proof the reload landed.

See [[Diagnosing a systemd service]], [[Unit files]]
