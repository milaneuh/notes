similarly to [[openssl x509 -req]] the ca command signs a CSR to produce a certificate, but it keeps record of what was issued, which lets it retroactively revoke certificates and generate Certificate Revocation Lists (CRLs). 

To set it up it needs a few files : a config file holding a `[ ca ]` section, which is where every path below is read from; `index.txt` to store the certificate database, which has to exist and be empty rather than absent; `serial` for the next serial number to use, which has to already hold a valid hex number such as `01`; and a `newcerts` directory which contains a copy of every certificate issued, named by its `serial` number. Generating CRLs needs a `crlnumber` file as well, on the same principle as `serial`.

Extensions are not carried over from the CSR on their own. `copy_extensions = copy` in the config section, or `-copy_extensions copy` on the command line, is what brings a [[Subject Alternative Name]] across.

See [[openssl x509 -req]], [[Certificates]], [[Public Key Infrastructure]]

## Cards
Q: what does `openssl ca` keep that `openssl x509 -req` does not, and what does that make possible?
A: a record of what it issued, in `index.txt`. That is what allows revocation and CRLs.

Q: which four things does `openssl ca` need in place before it can issue anything?
A: a config file with a `[ ca ]` section, `index.txt` present and empty, `serial` already holding a hex number, and a `newcerts` directory.

Q: where does `openssl ca` find the paths to `index.txt`, `serial` and `newcerts`?
A: in the `[ ca ]` section of its config file. It never guesses them.

Q: a SAN declared in the CSR is missing from the certificate `openssl ca` issued. What was left out?
A: `copy_extensions = copy` in the config, or `-copy_extensions copy` on the command line.
