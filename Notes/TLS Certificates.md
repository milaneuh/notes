---
tags: [pki]
---
A data structure holding a public key and a name, then signed. The signature
binds the key to the name: the *issuer* signs, the *subject* is named.

"Milan says John's public key is 01:02:03…", a claim by Milan about John,
which anyone holding Milan's public key can verify. That is the whole point:
trust one issuer's key in order to learn another entity's key.

See [[TLS Certificate main fields]], [[X.509]], [[Public Key Infrastructure]]
