The most common physical layer is an Ethernet network. There are different types of ethernet networks but they all have this in common : 

1. All devices on the ethernet network have a MAC address. 
2. All the data is wrapped in _frames_ which contains the sender and the receiver MAC address

Two ethernet networks cannot communicate with each other without an ethernet bridge. And the [[Network layer]] has to work on top of any physical layer, ethernet, wireless or modem, so the linux kernel provides a liaison between the two with the _kernel network interface(s)_. A network interface will link the IP address settings from the network layer with the hardware identification on the physical device. 

The traditional names are _eth0_ (First ethernet card in the computer) or _wlan0_ (wireless interface). 

Let's analyse this network interface : 
```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 52:55:55:90:be:05 brd ff:ff:ff:ff:ff:ff
    altname enx52555590be05
    inet 192.168.104.3/24 metric 200 brd 192.168.104.255 scope global dynamic eth0
       valid_lft 2743sec preferred_lft 2743sec
    inet6 fe80::5055:55ff:fe90:be05/64 scope link proto kernel_ll
       valid_lft forever preferred_lft forever
```

Each network interface gets a number, this one is `2`. That number is the interface index, or _ifindex_, and it can be read directly in `/sys/class/net/eth0/ifindex`. The flag `UP` means that the interface was brought up administratively, with `ip link set eth0 up`. `LOWER_UP` means that the physical link has a carrier, so the cable is plugged in and the driver confirms it. An interface can be `UP` without being `LOWER_UP`, and it then shows `NO-CARRIER` in its flags. 
## Cards
Q: what do all ethernet networks have in common?
A: every device on the network has a MAC address, and all the data is wrapped in frames that carry the sender and the receiver MAC address.

Q: what does a kernel network interface do?
A: it links the IP address settings of the network layer with the hardware identification of the physical device.

Q: in `2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>`, what is the `2`?
A: the interface index, the _ifindex_ the kernel gave to that interface. It can be read in `/sys/class/net/eth0/ifindex`.

Q: what does the flag `UP` mean on an interface?
A: the interface was brought up administratively, with `ip link set <name> up`.

Q: what does the flag `LOWER_UP` mean on an interface?
A: the physical link has a carrier. The cable is plugged in and the driver confirms it.

Q: an interface shows `UP` and `NO-CARRIER`, and no `LOWER_UP`. What happened?
A: it was configured and enabled, but there is no physical link. Cable unplugged, or the other end is dead.

Q: nothing on the network answers, and `ip addr show` prints the interface without the `UP` flag. Where do you look first?
A: nobody brought the interface up. Fix the administrative state before suspecting addresses, routes or names.

Q: two hosts on the same ethernet network exchange data. Which addresses does the frame carry?
A: the MAC address of the sender and the MAC address of the receiver.
