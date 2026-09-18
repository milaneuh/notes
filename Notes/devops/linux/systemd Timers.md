Timers are [[systemd]] [[Unit Files]] whos names end in .timer that control .service fies or event, they have the same file structure and a loaded form the same path but include a `[Timer]` section which defines when and how the timer activates. 

There is two times of Timers :
- Realtime Timers : activate on a calendar event, the same way [[cron|cronjobs]] do. To define them you use the `OnCalendar=` option.
- Monotomic Timers : activate after a time span relative to a varying starting point. They stop if the computer is temporarily suspended or shut down. There are a few different type of Monotomic Timers but all have the form: `OnTypeSec=`. Common ones include `OnBootSec` and `OnUnitActiveSec`

For each .timer file, a matching .service file exists. The .timer file activates and controls the .service file. The .service file does not require and `[Install]` section as it is the timer units that are enabled. 

Example : 

A timer which start 15min after boot and again every week while the system is running : 
```
[Unit]
Description=Run foo weekly and on boot

[Timer]
OnBootSec=15min
OnUnitActivateSec=1w

[Install]
WantedBy=timers.target
```


See :
- [[Timers vs cron]]