Although [[cron]] is the most well-known job scheduler, [[systemd Timers]] can be an alternative.

The main benefits of using Timers instead of cron are : 
- Jobs can be easily started independently of their timers. 
- Each job can be configured to run in a specific environmnent
- Jobs can be attached to [[cgroups]]
- Jobs can be set up to depend on other [[Unit Files|systemd Units]]
- Jobs are logged in the systemd Journal for easy debugging