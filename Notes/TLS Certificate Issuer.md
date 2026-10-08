---
tags: [pki]
---
The authority that verified the subject and signed with its private key,
expressed as a Distinguished Name.

The chain is built by equality: a certificate's `Issuer` matches the `Subject`
of the one above it. When the two are identical in the same certificate, it
signed itself, a root.

```
Issuer:  C=BE, O=GlobalSign nv-sa, CN=GlobalSign Root R46
Subject: C=BE, O=GlobalSign nv-sa, CN=GlobalSign Root R46   ← self-signed root
```

See [[TLS Certificate Subject]], [[TLS Certificate main fields]]
