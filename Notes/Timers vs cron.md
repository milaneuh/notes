---
tags: [linux, systemd]
---
cron is the time-based job scheduler, and whether it is even installed depends
on the distribution: Debian and Ubuntu ship it, Arch ships none and relies on
[[systemd Timers]]. Distrust any source saying "by default" without saying on
what.

What a timer buys over cron: the job can be started independently of its
schedule, run in a specific environment, be attached to [[cgroups]], depend on
other units, and it is logged in the journal like any unit, so it is debuggable
with the same tools.
