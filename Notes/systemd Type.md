---
tags: [linux, systemd]
---
The start-up types of a service unit:

- `simple`, the default: the service is considered started immediately.
- `forking`: started once the parent has forked and exited. Add `PIDFile=` so
  systemd can still track the main process.
- `oneshot`: for a script that does one job and exits. `RemainAfterExit=yes`
  keeps the unit Active afterwards.
- `notify`: like simple, except the daemon signals readiness itself, through a
  socket message and not a Unix signal.
- `dbus`: ready when the declared `BusName` appears on the system bus.
- `idle`: delays the binary until all jobs are dispatched, 5 seconds at most.
  Behaves like simple; the point is readable console output.

See [[Unit files]]
