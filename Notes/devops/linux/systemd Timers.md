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