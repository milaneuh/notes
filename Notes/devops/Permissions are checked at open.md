Permissions are evaluated once, when the file is **opened**. They are not checked again on every read or write.

So a running process keeps its access through a permission change : revoking a right does not affect a file descriptor that is already open. The process keeps working until it restarts and tries to open the file again.

This is the mechanism behind **latent failures** : `systemctl status` is green, the service answers, and the breakage only shows up at the next restart or reboot.

So after changing permissions or ownership of anything a service uses, restart the service and exercise the capability that failed. A service that still answers proves nothing about the change you just made.

See [[Permissions on a directory]], [[File ownership]]
