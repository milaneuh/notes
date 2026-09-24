When deciding between two routes, the kernel will always choose the one with the longest prefix. For example `192.168.0.0/16` matches and its prefix is `16` bits long but `192.168.104.0/24` also matches but its prefix, `24`, is longer so the rule for `192.168.104.0/24` takes priority.

The default route is `0.0.0.0/0`, a prefix of length zero. It matches every destination, and it loses against any other route that matches, which is why traffic only goes to the gateway when nothing more specific was found.

## Cards
Q: two routes in the table both match a destination. Which one does the kernel use?
A: the one with the longest prefix, so the most specific of the two.

Q: the table holds `default via 192.168.104.2` and `192.168.104.0/24 dev eth0 scope link`. Which rule applies to `192.168.104.50`, and which one to `1.1.1.1`?
A: `192.168.104.50` matches both, and `/24` is longer than the `/0` of the default route, so the link route wins and the host talks to it directly. `1.1.1.1` matches only the default route, so the packet goes to the gateway.
