Connecting subnets is simply a process of sending data through hosts connected to more than one subnet. 

For example let's say you have this network : 
```
subnet : 192.168.104.0/24
router : 192.168.104.2
host_a : 192.168.104.1
host_b : 192.168.104.3
```

For host a to communicate to host b it can directly reach it because they are on the same subnet. But for host a to reach other hosts on the rest of the internet, it must communicate through the router. 

The linux kernel distinguishes between these two different kinds of destinations by using a `routing table` to determine its routing behaviour. To show the routing table, use the `ip route show` command. 

For example :
```bash
$ ip route show
default via 192.168.104.2 dev eth0 proto dhcp src 192.168.104.1 metric 200
192.168.104.0/24 dev eth0 proto kernel scope link src 192.168.104.1 metric 200
192.168.104.2 dev eth0 proto dhcp scope link src 192.168.104.1 metric 200
```

Each line in this output is a routing rule, let's start with the second line and break it into fields.  

The first field we encounter is `192.168.104.0/24`, which is a destination network. As with previous examples, this is the host's local subnet. This rule says that the host can reach the local subnet directly though it's network. 

The first line of output is the destination network `default route`. It means that the traffic using the default route is to be sent to `192.168.104.2`; `dev eth0` indicates that the physical transmission will happen on that network interface; `proto dhcp` is where the route came from, a dhcp client installed it using the gateway the DHCP server handed out; `src 192.168.104.1` is the preferred route address, the local IP kernel puts in outgoing packets that use this route; `metric 200` is the route weight, if we have multiple routes on the same destination, the one with the _lowest_ weight wins. 

The third route is almost the same as the first one, the differences being `scope link` meaning that the route is on the directly attached network. 

To summarise : 

1. `default via 192.168.104.2 ... proto dhcp` this has global scope. Anything not matched by another specific route will go there
2. `192.168.104.0/24 dev eth0 proto kernel scope link` The subnet local link. 
3. `192.168.104.2 dev eth0 proto dhcp scope link` An host route to the gateway itself and the DHCP client added it. 


## Cards
Q: how do you connect two subnets?
A: by sending data through a host that is connected to more than one subnet.

Q: what does the kernel use to tell a destination on the local subnet apart from one that has to go through a router?
A: the routing table.

Q: which command shows the routing table?
A: `ip route show`.

Q: in a route line, what does `dev eth0` mean?
A: the physical transmission for this route happens on that network interface.

Q: in a route line, what does `proto dhcp` mean?
A: where the route came from. A DHCP client installed it, using the gateway the DHCP server handed out.

Q: in a route line, what does `src 192.168.104.1` mean?
A: the preferred source address, the local IP the kernel puts in outgoing packets that use this route.

Q: in a route line, what does `metric 200` mean?
A: the weight of the route. When several routes lead to the same destination, the lowest weight wins.

Q: what does `scope link` mean on a route?
A: the destination sits on the directly attached network, so it is reachable without a gateway.

Q: what does `via` on a route mean, compared to `scope link`?
A: `via` names the gateway the packet is handed to. `scope link` means the host reaches the destination itself.
