`req` and `x509` are two separate openssl subcommands. `openssl req` creates a certificate signing request (CSR). `openssl x509` works on certificates, and its `-req` option tells it that its input is a CSR rather than an existing certificate :

```
$ openssl x509 -help
 -req    Input is a CSR file (rather than a certificate)
```

So `openssl x509 -req` signs a CSR to produce a certificate, the same job as [[openssl ca]] without the bookkeeping. It keeps no record of what it issued, so serial numbers are the operator's problem and nothing stops two certificates going out with the same one.

It also drops the extensions of the CSR unless `-copy_extensions copy` is passed, which silently loses the [[Subject Alternative Name]].

See [[openssl ca]], [[Certificates]], [[Public Key Infrastructure]]

## Cards
Q: `openssl req` and `openssl x509 -req`, what does each one do?
A: `openssl req` creates a CSR. `openssl x509 -req` reads a CSR and signs it into a certificate.

Q: `-req` is an option of which subcommand, and what does it change?
A: of `x509`. It tells it that its input is a CSR rather than an existing certificate.

Q: what becomes the operator's problem when issuing with `openssl x509 -req`?
A: serial numbers. It keeps no record, so nothing stops two certificates going out carrying the same one.

Q: you sign a CSR that declares a SAN and the certificate comes out without one. Why?
A: extensions are not carried over unless `-copy_extensions copy` is passed.
