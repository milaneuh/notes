similarly to [[openssl x509 -req]] the ca command signs a CSR to produce a certificate, but it keeps record of what was issued, which lets it retroactively revoke certificates and generate Certificate Revocation Lists (CRLs). 

To set it up it needs a few files : a config file holding a `[ ca ]` section, which holds almost nothing itself beyond `default_ca`, the name of the section where every path below is actually read from; `index.txt` to store the certificate database, which has to exist rather than be absent, empty or not; `serial` for the next serial number to use, which has to already hold a valid hex number with an even count of digits, so `01` works where `1` fails on a `short line` error that names the wrong problem; and a `newcerts` directory which contains a copy of every certificate issued, named by its `serial` number. Two config keys are mandatory on top of the paths: `default_md` for the signature digest, which is the first thing the command stops on when it is missing, and `policy`, which has to name a section that exists. Generating CRLs needs a `crlnumber` file as well, on the same principle as `serial`.

Extensions are not carried over from the CSR on their own. `copy_extensions = copy` in the config section is what brings a [[Subject Alternative Name]] across. There is no command line equivalent here, `copy_extensions` is absent from `openssl ca -help`, and only `openssl x509` takes it as a flag.

See [[openssl x509 -req]], [[Certificates]], [[Public Key Infrastructure]]

## Cards
Q: what does `openssl ca` keep that `openssl x509 -req` does not, and what does that make possible?
A: a record of what it issued, in `index.txt`. That is what allows revocation and CRLs.

Q: which things does `openssl ca` need in place before it can issue anything?
A: a config file whose `[ ca ]` section names a real settings section through `default_ca`, carrying `default_md` and a `policy` that points at a section that exists; `index.txt` present; `serial` already holding an even digit hex number; and a `newcerts` directory.

Q: where does `openssl ca` find the paths to `index.txt`, `serial` and `newcerts`?
A: in the section named by `default_ca`, not in `[ ca ]` itself. `[ ca ]` only carries `default_ca`, `RANDFILE`, `preserve` and `msie_hack`. It never guesses the paths.

Q: a SAN declared in the CSR is missing from the certificate `openssl ca` issued. What was left out?
A: `copy_extensions = copy` in the config section named by `default_ca`. There is no command line flag for it on `openssl ca`.
