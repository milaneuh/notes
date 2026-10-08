---
tags: [pki, networking]
---
The X.509v3 extension listing the names a certificate is valid for, and the
only field a TLS client matches a requested hostname against. Entries are
typed, and the type is part of the match: DNS names in preferred name syntax
as IA5String, IP addresses in network byte order as OCTET STRING.

```
X509v3 Subject Alternative Name:
    DNS:github.com, DNS:www.github.com
```

**A present SAN makes the CN ignored entirely.** `CN=shop.example.com` with a
SAN listing only `api.example.com` covers `api.example.com` and nothing else.
Since RFC 9525 (2024, obsoleting 6125) there is no fallback at all, so a
certificate with no SAN is simply rejected on the name. A root CA carries none:
nobody matches a hostname against an authority.

Signature, dates and chain are a separate set of checks. All three can pass
while the name is still rejected, and then the SAN is where to look.

```bash
openssl x509 -noout -ext subjectAltName -in cert.pem   # LibreSSL on macOS lacks -ext
openssl x509 -noout -text                              # portable fallback
openssl s_client -connect host:443 -servername name    # what the server really sends
curl -s -o /dev/null -w '%{ssl_verify_result}\n' https://host/   # 0 = verified
```

See [[TLS Certificate Extensions]], [[TLS Certificate Subject]], [[Host header]]
