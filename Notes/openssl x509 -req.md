---
tags: [pki, tooling]
---
`req` and `x509` are two separate subcommands: `openssl req` creates a
certificate signing request, `openssl x509` works on certificates, and `-req`
tells it its input is a CSR rather than an existing certificate.

```
$ openssl x509 -help
 -req    Input is a CSR file (rather than a certificate)
```

So it signs a CSR into a certificate, the same job as [[openssl ca]] without
the bookkeeping. It keeps no record of what it issued, so serial numbers are
the operator's problem and nothing stops two certificates going out with the
same one. It also drops the CSR's extensions unless `-copy_extensions copy` is
passed, silently losing the [[Subject Alternative Name]].

See [[openssl ca]]
