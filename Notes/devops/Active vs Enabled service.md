An [[Unit Files|unit]] in [[systemd]] can be both Active or Inactive but it can also be Enabled or Disabled. The difference is simple : 

- An Active unit is currently running, an Inactive one is not.
- An Enabled unit is currently configured to boot up when the system starts, a Disabled one is not

An unit can be both Active and Disabled or vice versa. So a service can answer perfectly today and be gone after the next reboot.

See [[Enable a service]] for what Enabled actually is on disk.

## Cards
Q: Active vs Inactive, for a systemd unit?
A: an Active unit is currently running, an Inactive one is not.

Q: Enabled vs Disabled, for a systemd unit?
A: an Enabled unit is configured to start when the system boots, a Disabled one is not.

Q: can a unit be Active and Disabled at the same time?
A: yes. A service can answer perfectly today and be gone after the next reboot.

Q: are units only services?
A: no — there are around a dozen types: `service`, `timer`, `socket`, `mount`, `target`, `path`.
