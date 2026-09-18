Although [[cron]] is the most well-known job scheduler, [[systemd Timers]] can be an alternative.

The main benefits of using Timers instead of cron are : 
- Jobs can be easily started independently of their timers. 
- Each job can be configured to run in a specific environmnent
- Jobs can be attached to [[cgroups]]
- Jobs can be set up to depend on other [[Unit Files|systemd Units]]
- Jobs are logged in the systemd Journal for easy debugging

## Cards
Q: why would you use a systemd timer instead of cron?
A: the job can be started independently of its timer, configured in a specific environment, attached to cgroups, and made to depend on other units.

Q: what does a systemd timer give you that cron does not, when a job misbehaves?
A: the job is logged in the systemd journal, so it is debuggable with the same tools as any other unit.
