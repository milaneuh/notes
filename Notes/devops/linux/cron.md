cron is the time-based job scheduler in [[linux]]. It enables users to schedule jobs -- such as commands or shell scripts -- to run periodically at certain times. 

There are many cron implementations. Whether one is installed by default depends on the distribution : on Debian and Ubuntu `cron` is there out of the box, on Arch none of them are and the base system relies on [[systemd Timers]] instead.

Beware of any source that says "by default" without saying on what.

See : 
- [[Timers vs cron]]