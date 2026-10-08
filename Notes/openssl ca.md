---
tags: [pki, tooling]
---
Signs a CSR like [[openssl x509 -req]], but keeps a record of what it issued:
`index.txt` plus a copy in `newcerts/`. That record is what makes revocation
and CRLs possible at all.

What it needs before it will sign anything:

- a config whose `[ ca ]` section names a real section through `default_ca`.
  `[ ca ]` itself holds almost nothing else; the paths and the mandatory
  `default_md` and `policy` all live in the section it points at, and it never
  guesses them.
- `index.txt` present, empty is fine.
- `serial` already holding a hex number with an **even** digit count: `01`
  works where `1` fails on a `short line` error that names the wrong problem.
- a `newcerts/` directory. CRLs want a `crlnumber` file on the same principle.

Extensions are not carried over on their own: `copy_extensions = copy` in the
section named by `default_ca` is what brings a
[[Subject Alternative Name]] across. There is no command line flag: it is
absent from `openssl ca -help`, only `openssl x509` takes one.

See [[openssl x509 -req]], [[Public Key Infrastructure]]
