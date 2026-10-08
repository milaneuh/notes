---
tags: [networking, linux]
---
The linux firewall. Tables hold chains, chains hold rules; a table is a
namespace whose address family decides which packets it processes. In practice
`inet`, covering v4 and v6 at once; the other families exist for arp, bridge
and netdev.

During an incident the firewall answers one question, is it responsible, and
the default answer is no: **I prove its innocence, I never assume its guilt.**

A rule can name my port and never see my traffic.
`iifname != "lo" tcp dport 8080 drop` skips loopback, so a local test never
meets it. Before accusing a rule: which interface, which direction, which
address family, and did an earlier rule already accept the packet. Rules are
ordered, so read the ruleset and not the line you grepped for.

The empirical proof is the counter, and only rules carrying a `counter`
statement have one. Reset, reproduce the failure, look again: zero packets is a
proof, not an opinion.

The firewall also shows itself in the delay. A DROP discards and nothing
answers, so the connection hangs; a REJECT answers immediately and looks exactly
like a port where nobody listens. A delay proves a filter, the absence of one
proves nothing.

Never flush the ruleset to see what happens: that destroys the running state,
which is the observation you came for. Delete a single rule by its handle and
put it back. And the kernel ruleset is runtime state, `/etc/nftables.conf`
loaded by `nftables.service` is the declared source, so a rule added by hand
does not survive a reboot and one deleted by hand comes back.

```bash
nft list ruleset -a     # handles and counters
nft reset counters
nft delete rule inet filter input handle <n>
```

See [[Configured state vs running state]], [[Listening address]]
