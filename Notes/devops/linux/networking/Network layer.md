The network layer also known as the internet layer is the base of the internet as we currently know it.  The goal of the internet layer is to send and receive internet packets regardless of the hardware or operating system.

The internet layer uses two different versions of the internet protocol (IP), the ipv6 and the ipv4. 

Every internet host has at least one IP address. For IPv4 it is in the form `a.b.c.d`, such as `10.23.2.37`. An address in this notation is called a _dotted-quad_ sequence. If the host is connected to multiple subnets, it will have at least one ip address for each subnet. 

## Viewing IP Addresses
Since one machine can have multiple IP addresses, you can list them using this command : 

```bash
ip addr show
```

It will often have multiple responses but it should look something like this : 

```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 52:55:55:8e:6d:c6 brd ff:ff:ff:ff:ff:ff
    altname enx5255558e6dc6
    inet 192.168.104.1/24 metric 200 brd 192.168.104.255 scope global dynamic eth0
       valid_lft 2377sec preferred_lft 2377sec
    inet6 fe80::5055:55ff:fe8e:6dc6/64 scope link proto kernel_ll
       valid_lft forever preferred_lft forever
```

On the fourth line you can see that the host is configured with an IPv4 address (denoted with inet) of `192.168.104.1`. The `/24` after the address helps define the [[subnets]] that that the IP address belongs to.

See [[subnets]]

## Cards
Q: what is the other name of the network layer?
A: the internet layer.

Q: what is the goal of the internet layer?
A: to send and receive internet packets regardless of the hardware or the operating system.

Q: how many IP addresses does an internet host have?
A: at least one, and at least one per subnet when it is connected to several.

Q: what is a dotted-quad sequence?
A: the IPv4 notation `a.b.c.d`, for example `10.23.2.37`.

Q: which command lists the IP addresses of a machine?
A: `ip addr show`.

Q: in the output of `ip addr show`, which keyword marks an IPv4 address?
A: `inet`. IPv6 addresses are marked `inet6`.

Q: in `inet 192.168.104.1/24`, what does the `/24` tell you?
A: the subnet the address belongs to.

Q: `ip addr show` prints an `inet6 fe80::...` line and no `inet` line for an interface. What do you know?
A: the interface holds no IPv4 address, only an IPv6 link local one.

Q: a host shows three IP addresses. What does that tell you about its connectivity?
A: it is most likely attached to several subnets, since a host holds at least one address per subnet it is connected to.

Q: you read `10.23.2.37` in a configuration file. Which version of IP, and how do you know?
A: IPv4. It is a dotted-quad sequence, four numbers in the `a.b.c.d` form.
