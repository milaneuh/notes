systemd is a software suite for system and service management in [[linux]].

It describes how to manage each unit in [[Unit Files]]. A unit is not only a service : there are around a dozen types, `service`, `timer`, `socket`, `mount`, `target`, `path`. And a unit file is not the configuration of the daemon itself, it is the description of how systemd should manage it.

- [[Active vs Enabled service]] running now, versus starting at boot
- [[Enable a service]] what Enabled is on disk
- [[Unit files are cached]] why editing a unit is not enough
- [[systemd StateDirectory]] declaring a service state directory instead of chmod
- [[Diagnosing a systemd service]] the order to follow when it breaks
- [[systemd exit codes]] who failed, and therefore where to look

The options for an unit are :
	-[[systemd StateDirectory|StateDirectory]] # creates the named directories below `/var/lib` 
	- [[systemd Type|Type]] # define the Type of an unit 
