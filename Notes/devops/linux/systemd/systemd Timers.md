Timers are [[systemd]] [[Unit Files]] whose names end in .timer that control .service files or events, they have the same file structure and are loaded from the same paths but include a `[Timer]` section which defines when and how the timer activates. 

There are two types of Timers :
- Realtime Timers : activate on a calendar event, the same way [[cron|cronjobs]] do. To define them you use the `OnCalendar=` option.
- Monotonic Timers : activate after a time span relative to a varying starting point. They stop if the computer is temporarily suspended or shut down. There are a few different type of Monotonic Timers but all have the form: `OnTypeSec=`. Common ones include `OnBootSec` and `OnUnitActiveSec`

For each .timer file, a matching .service file exists. The .timer file activates and controls the .service file. The .service file does not require an `[Install]` section as it is the timer units that are enabled. 

Example : 

A timer which start 15min after boot and again every week while the system is running : 
```
[Unit]
Description=Run foo weekly and on boot

[Timer]
OnBootSec=15min
OnUnitActiveSec=1w

[Install]
WantedBy=timers.target
```


See :
- [[Timers vs cron]]

## Cards
Q: what is a systemd timer?
A: a unit whose name ends in .timer, with a `[Timer]` section, that controls a .service file or event. Same file structure and same paths as any other unit.

Q: what are the two types of systemd timer?
A: realtime timers, activated on a calendar event with `OnCalendar=`, and monotonic timers, activated after a time span relative to a varying starting point, with options of the form `OnTypeSec=`.

Q: give two monotonic timer options.
A: `OnBootSec` and `OnUnitActiveSec`.

Q: you have a .timer and its matching .service. Which one do you enable?
A: the timer. The .service does not need an `[Install]` section, because it is the timer unit that gets enabled.

Q: what happens to a monotonic timer if the machine is suspended or shut down?
A: it stops.
