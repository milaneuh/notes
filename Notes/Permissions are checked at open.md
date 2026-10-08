---
tags: [linux, filesystem, permissions]
---
Permissions are evaluated once, when the file is opened, and never again per
read or write. Revoking access does nothing to a file descriptor that is
already open.

That is what makes a permission change a latent failure: `systemctl status`
stays green and the service keeps answering on its open descriptors, while the
breakage waits for the next restart or reboot. After changing permissions or
ownership, restart the service and exercise the capability. A service that
still answers proves nothing.

See [[Unix permissions]], [[Diagnosing a systemd service]]
