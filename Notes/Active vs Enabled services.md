An [[Unit Files|unit]] in [[systemd]] can be both Active or Inactive but it can also be Enabled or Disabled. The difference is simple : 

- An Active unit is currently running, an Inactive one is not.
- An Enabled unit is currently configured to boot up when the system starts, a Disabled one is not

An unit can be both Active and Disabled or vice versa. So a service can answer perfectly today and be gone after the next reboot.

See [[Enable a service]] for what Enabled actually is on disk.
