A configuration file on disk and the state of the process that is supposed to obey it are two different sources of truth. They agree only after a reload that actually succeeded. Everything in between is a place where a diagnosis goes wrong, because the file says what you meant and the service does what it was last told.

I have now hit this twice, in two different domains.

On `catalog-reports`, `cat` on the unit file I had written myself showed a clean unit, while `systemctl cat` and `systemctl show -p` showed a `TasksMax=1` coming from a drop in I had never opened. The file I was reading was not the configuration the service was running.

On `bind9`, `named-checkconf -z` reported `zone catalog.lab/IN: loaded serial 2026092601` with no error, while `dig @127.0.0.1 srv-dns.catalog.lab` answered `NXDOMAIN`. The validator reads the file on disk. `dig` asks the process in memory. The zone was correct and the server had not reloaded.

## The discipline

Validate the file, reload the service, then interrogate the service. Three steps, and skipping the third is what produces the false feeling of having applied something.

A reload on a broken configuration is the worst case, because it leaves the previous configuration running. Nothing visibly fails and nothing has changed.

## A related trap

`systemctl status` prints the last ten journal lines of the unit. For a service that has been running quietly for hours, those ten lines are the ones from **startup**. They can look like an ongoing failure while describing a moment long past. Check their timestamps against the `Active: since` line before believing them, and use `journalctl -u <unit> --since -10min` to see what is happening now.

*À compléter : combien de temps j'ai perdu à cause de ça, les deux fois.*

## Tooling

Validators, to run before every reload :

- `sshd -t` : syntax of `sshd_config`, though it fails on a socket activated `sshd`, where `sshd -T` still works
- `named-checkconf -z` : parses the bind9 configuration and loads every zone
- `named-checkzone <zone> <file>` : one zone file on its own
- `nginx -t` : the whole nginx configuration

Instruments that show the effective state rather than the intention :

- `systemctl cat <unit>` : the unit plus every drop in, in the order they apply
- `systemctl show -p <property> <unit>` : the value the manager actually holds
- `named-compilezone -f text -F text -o - <zone> <file>` : the zone after the origin has been appended, so what the file really became
- `nginx -T` : the configuration as nginx assembled it, includes resolved
- asking the service itself, with `dig`, `curl` or `ss`, which is the only proof that the reload landed

See [[Unit files are cached]], [[Diagnosing a systemd service]], [[name resolution]], [[reverse proxy]]

## Cards
Q: a configuration file on disk and the running process, when do they agree?
A: after a reload that succeeded. Before that they are two different sources of truth.

Q: why is validating a file not enough?
A: a validator reads the file on disk. It says nothing about what the running process currently holds in memory.

Q: what happens when you reload a service whose configuration is broken?
A: the previous configuration stays in place. Nothing visibly fails, and nothing has changed either.

Q: the three steps after editing a service's configuration?
A: validate the file, reload the service, then interrogate the service to prove the reload landed.

Q: `named-checkconf -z` loads your zone without error and `dig` answers `NXDOMAIN`. What is wrong?
A: nothing in the file. The running server has not reloaded it.

Q: `systemctl status` shows what look like errors repeating. What do you check before believing it?
A: the timestamps of those lines against `Active: since`. Status prints the last ten journal lines, which for a long running quiet service are the startup ones.

Q: which command shows a systemd unit's configuration as the manager assembled it, drop ins included?
A: `systemctl cat`. A `cat` on the file you wrote yourself shows only your half.
