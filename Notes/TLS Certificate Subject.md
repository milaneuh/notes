---
tags: [pki]
---
The entity the certificate identifies, as an X.500 **Distinguished Name** built
from RDN attributes:

| RDN | meaning |
|---|---|
| CN | Common Name, a readable label (`Catalog Lab Root CA`) |
| O | the legal organisation |
| OU | a division, largely deprecated by the CA/Browser Forum |
| C | two-letter ISO country |
| ST | state or province |
| L | locality, the city |

The CN used to carry a hostname. RFC 9525 forbids using it to identify a
service, so on a leaf it is decorative and on an authority it is there to be
read, the name check happens in the [[Subject Alternative Name]].

See [[TLS Certificate Issuer]], [[TLS Certificate main fields]]
