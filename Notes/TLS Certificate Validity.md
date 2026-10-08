---
tags: [pki]
---
`Not Before` and `Not After`, in UTC. A client rejects a certificate outside
that window whatever else is correct, and roots are long-lived where leaves are
not, the GlobalSign root below runs 2019 → 2046, a Web PKI leaf is capped
around 13 months.

```
Validity
    Not Before: Mar 20 00:00:00 2019 GMT
    Not After : Mar 20 00:00:00 2046 GMT
```

See [[TLS Certificate main fields]]
