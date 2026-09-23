nftables is the linux firewall and packet filtering tool. It uses tables to store chains. The chains contain individual rules for performing actions. A table is the namespace that contains a collection of chains, rules and sets, and its address family defines the packet types it processes. In practice I write `inet`, which covers ip and ipv6 at once, the other families exist for arp, bridge and netdev traffic.

During an incident the firewall only answers one question : is it responsible for what I see, yes or no. The default answer is no and the burden of proof is on me. I prove the innocence of the firewall, I never assume its guilt.

A rule can name my port and never see my traffic. `iifname != "lo" tcp dport 8080 drop` skips everything coming through [[loopback]], so a local test never meets it. Before accusing a rule I have to show that it applies to my traffic : which interface, which direction, which address family, and whether an earlier rule in the chain already accepted the packet. Rules are ordered, so I read the whole ruleset and not the line I grepped for.

The empirical proof is the counters. A rule only counts if it carries a `counter` statement, and `nft list ruleset` then shows how many packets it matched. I reset the counters, reproduce the failure, then look again : zero packet on the rule is a proof, not an opinion.

The firewall shows itself through the delay. A DROP discards the packet and nothing ever answers, so the connection hangs for several seconds. A REJECT answers immediately, which looks exactly like a port where nobody listens. A delay proves there is a filter, the absence of delay proves nothing.

I never flush the ruleset to see what happens. It destroys the running state, which is the observation I am trying to make. To test one rule I delete it by its handle and put it back.

The ruleset in the kernel is runtime state, `/etc/nftables.conf` loaded by `nftables.service` is the declared source. A rule added with `nft add rule` does not survive a reboot, and a rule deleted by hand comes back at the next one.

## Tooling

- `nft list ruleset -a` : the whole ruleset, with the handle of each rule and the counters of the rules that carry one
- `nft reset counters` : zero the counters before reproducing the failure
- `nft delete rule <family> <table> <chain> handle <n>` : remove one rule instead of flushing

## Cards
Q: during an incident, what is the only question the firewall answers?
A: whether it is responsible for what I see. The default answer is no, and the burden of proof is on me.

Q: a rule names my port. Is it guilty?
A: not yet. I have to show it applies to my traffic: which interface, which direction, which address family, and whether an earlier rule already accepted the packet. `iifname != "lo" tcp dport 8080 drop` never meets a local test.

Q: what is the empirical proof that a rule matched?
A: its counter, and only if the rule carries a `counter` statement. Reset, reproduce the failure, look again. Zero packet is a proof, not an opinion.

Q: DROP and REJECT, how do I tell them apart from the client side?
A: DROP discards and nothing answers, so the connection hangs. REJECT answers immediately and looks exactly like a port where nobody listens.

Q: why do I never flush the ruleset during an incident?
A: flushing destroys the running state, which is the observation I am trying to make. I delete a single rule by its handle and put it back.

Q: does a rule added with `nft add rule` survive a reboot?
A: no. The kernel ruleset is runtime state, `/etc/nftables.conf` loaded by `nftables.service` is the declared source.
