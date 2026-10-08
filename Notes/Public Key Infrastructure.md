---
tags: [pki]
---
The umbrella term for the practices around issuing, distributing, storing and
using certificates and keys. Vague on purpose; what matters is which one you
are in.

- **Web PKI** works by default in browsers and anything speaking TLS. In
  exchange it fixes the name rules, the algorithms, the validity periods,
  revocation and path validation.
- **Internal PKI** hands all of that back to you, lifetime, revocation,
  renewal, key types, for services, containers, VMs and hardware. It is also
  the only option for an internal IP or a name absent from the global DNS,
  which Web PKI has no way to verify and will not sign.

See [[X.509]], [[TLS Certificates]]
