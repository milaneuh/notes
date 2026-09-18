There are multiple start-up type to consider when writing a custom unit file. 
There types are : 

- simple (default) : [[systemd]] considers the service to be started immediately. 
- forking : systemdd considers the service once the parent process forks and the parent has exited. You should specify `PIDFile=` as well so systemd can keep track of the main process 
- oneshot : this is useful for scripts that do a single job and then exit.  If you want systemd to stll consider the service as [[active|active]] even after the process exited you can set `RemainAfterExit=yes`
- notify : identical to simple but the daemon will send a signal to systemd when it is ready to be started up
- dbus : the service is considered ready when the specified `BusName` appears of DBus's system bus.
- idle : systemd wil ldelay execution of the service binary until all jobs are dispatched unless these take long than 5, where the service binary is started anyway. The behaviour is very similar to simple, the main use-case for idle is for console output readability.