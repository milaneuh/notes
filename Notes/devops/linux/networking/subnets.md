A subnet is a connected group of hosts in a certain range of ip addresses. For example, the hosts in the range `192.168.2.1` to `192.168.2.31` could comprise a subnet, as could all hosts between `192.168.2.1` to `192.168.2.255`. As could all hosts between `192.168.1.1` and `192.168.255.255`.  

## CIDR Notation 
Another subnet notation is *Classless-Inter-Domain-Routing*, where a subnet such as `192.168.104.0/255.255.255.0` is written as `192.168.104.0/24`. This notation identifies the subnet mask by the number of leading bits set to 1 in the subnet mask. 

For example :

| Long form         | CIDR Form |
| ----------------- | --------- |
| `255.0.0.0`       | `/8`      |
| `255.255.0.0`     | `/16`     |
| `255.240.0.0`     | `/12`     |
| `255.255.255.0`   | `/24`     |
| `255.255.255.192` | `/26`     |

A mask is always a continuous run of 1 bits followed by a continuous run of 0 bits, so an octet in a mask can only be 0, 128, 192, 224, 240, 248, 252, 254 or 255.

See [[Routes and Routing Tables]]

## Cards
Q: what is a subnet?
A: a connected group of hosts inside a certain range of IP addresses.

Q: what does CIDR stand for?
A: Classless Inter-Domain Routing.

Q: in CIDR notation, what does the number after the slash count?
A: the number of leading bits set to 1 in the subnet mask. `/24` means 24 bits.

Q: how many bits does an IPv4 address hold, and what range can a prefix length take?
A: 32 bits, so a prefix goes from `/0` to `/32`.

Q: write `255.255.0.0` in CIDR form.
A: `/16`.

Q: write `/26` in long form.
A: `255.255.255.192`.

Q: why can an octet of a subnet mask never be 210?
A: a mask is a continuous run of 1 bits followed by a continuous run of 0 bits. 210 is `11010010`, which breaks the run. Only 0, 128, 192, 224, 240, 248, 252, 254 and 255 are legal.

Q: someone writes `255.192.255.0` as a subnet mask. What is wrong with it?
A: a mask is a continuous run of 1 bits followed by a continuous run of 0 bits. Once a 0 bit appears you cannot go back to 1, so this one is not a mask at all.

Q: two hosts are configured as `192.168.104.10/24` and `192.168.105.10/24`. Same subnet?
A: no. A `/24` fixes the first three octets, and 104 is not 105. They need a router to reach each other.

Q: you are told a subnet holds 256 addresses. What prefix length is it?
A: `/24`. 32 bits total minus 8 bits left free for hosts.

Q: a machine has the address `192.168.104.9` and the mask `255.255.255.0`. Write the subnet it belongs to.
A: `192.168.104.0/24`.
