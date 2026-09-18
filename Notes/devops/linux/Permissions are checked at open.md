Permissions are evaluated once, when the file is **opened**. They are not checked again on every read or write.

So a running process keeps its access through a permission change : revoking a right does not affect a file descriptor that is already open. The process keeps working until it restarts and tries to open the file again.

This is the mechanism behind **latent failures** : `systemctl status` is green, the service answers, and the breakage only shows up at the next restart or reboot.

So after changing permissions or ownership of anything a service uses, restart the service and exercise the capability that failed. A service that still answers proves nothing about the change you just made.

See [[Permissions on a directory]], [[File ownership]]

## Cards
Q: when are file permissions evaluated?
A: once, when the file is **opened**. Not again on every read or write.

Q: what happens to a running process when you revoke its access to a file it has open?
A: nothing. The already-open file descriptor keeps working. The breakage only appears when the process restarts and opens the file again.

Q: what is a latent failure?
A: `systemctl status` is green and the service answers, but the permission change you made already broke it — it will only surface at the next restart or reboot.

Q: what must you do after changing permissions or ownership of anything a service uses?
A: restart the service and exercise the capability that failed. A service that still answers proves nothing about the change you just made.
