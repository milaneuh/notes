---
tags: [linux, systemd]
---
A unit whose name ends in `.timer`, with a `[Timer]` section, driving a
`.service`. Same file structure and same paths as any other unit.

```ini
[Timer]
OnBootSec=15min
OnUnitActiveSec=1w
[Install]
WantedBy=timers.target
```

Two kinds: **realtime** timers fire on a calendar event with `OnCalendar=`,
**monotonic** timers after a span relative to a moving point (`OnBootSec`,
`OnUnitActiveSec`) and stop while the machine is suspended or off.

You enable the timer, not the service it drives; the `.service` needs no
`[Install]` section.

See [[Timers vs cron]]
