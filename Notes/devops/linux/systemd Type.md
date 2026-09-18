There are multiple start-up type to consider when writing a custom unit file. 
These types are : 

- simple (default) : [[systemd]] considers the service to be started immediately. 
- forking : systemd considers the service once the parent process forks and the parent has exited. You should specify `PIDFile=` as well so systemd can keep track of the main process 
- oneshot : this is useful for scripts that do a single job and then exit.  If you want systemd to still consider the service as [[Active vs Enabled service|active]] even after the process exited you can set `RemainAfterExit=yes`
- notify : identical to simple but the daemon tells systemd when it is ready to be started up. Note that this is a notification sent on a socket, not a Unix signal.
- dbus : the service is considered ready when the specified `BusName` appears on DBus's system bus.
- idle : systemd will delay execution of the service binary until all jobs are dispatched, unless these take longer than 5 seconds, where the service binary is started anyway. The behaviour is very similar to simple, the main use-case for idle is for console output readability.