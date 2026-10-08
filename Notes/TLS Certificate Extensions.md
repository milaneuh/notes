---
tags: [pki]
---
The X.509 v3 fields. The ones worth reading:

- **Key Usage**: what the key may do. `Certificate Sign` is what makes it a CA
  key, and it has to agree with Basic Constraints.
- **Basic Constraints**: `CA:TRUE` or not.
- **Subject Key Identifier / Authority Key Identifier**: identify the
  subject's key and the issuer's. A certificate with an SKI and no AKI has no
  separate issuer key to point at, which fits a self-signed root.
- **[[Subject Alternative Name]]**: the names the certificate is valid for.

An extension marked `critical` means fail-closed: a client that cannot
understand it must reject the certificate.

See [[TLS Certificate main fields]]
