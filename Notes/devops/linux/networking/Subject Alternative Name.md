A certificate declares the names it is valid for in an X.509v3 extension named `subjectAltName`, the SAN. A TLS client compares the name it was asked to reach against the entries of that list, and rejects the certificate when none of them match.

Entries are typed, and the type is part of the match :

```
X509v3 Subject Alternative Name:
    DNS:github.com, DNS:www.github.com
```

The SAN value type is GeneralName, it can have multiple values but the two that matters for me are :
	If the SAN is a DNS it must be written in the "preferred name syntax" as a IA5String.
	If the SAN is an IP address it must be written in "network byte order" as a OCTET STRING

## The CN is not the field that is checked

For example : `github.com` serves a single certificate whose `Subject` names only one of the two names that certificate covers :

```
$ echo | openssl s_client -connect github.com:443 -servername github.com 2>/dev/null \
    | openssl x509 -noout -subject -text | grep -E 'subject=|Alternative' -A1
subject= /CN=github.com
            X509v3 Subject Alternative Name:
                DNS:github.com, DNS:www.github.com
```

`https://www.github.com` is accepted all the same :

```
$ curl -s -o /dev/null -w '%{http_code} %{ssl_verify_result}\n' https://www.github.com/
301 0
```

`ssl_verify_result` at 0 means the validation succeeded. The 301 is an application redirect, which can only happen once the handshake is already done.

When a SAN is present the client compares against the SAN and ignores the CN completely. And since RFC 9525 of 2024, which obsoletes RFC 6125, there is no fallback left : its section 2 says `The Common Name RDN MUST NOT be used to identify a service`, and extends that to the other RDNs of the `subjectName`. A certificate carrying no SAN is rejected on the name.
## The SAN and the Subject field

A root certification authority carries a `Subject` and no SAN at all. The GlobalSign root dumped in [[Certificates]] shows it.


The `Subject` is expressed as an X.500 **Distinguished Name (DN)**, which consists of structured relative distinguished name (RDN) attributes: 
- **CN (Common Name):** a readable label for the entity (example : Catalog Lab Root CA). It used to carry a server hostname, and RFC 9525 forbids using it to identify a service, so on a leaf it is decorative and on an authority it is there to be read.
- **O (Organization):** The legal name of the company or organization. 
- **OU (Organizational Unit):** A division or department within the organization (now largely deprecated by the CA/Browser Forum).
- **C (Country):** Two-letter ISO country code where the organization is located. 
- **ST / S (State or Province):** The state, region, or province. 
- **L (Locality):** The city or town
It describes the entity the certificate identifies

The `Issuer` is also expressed as a DN. It describes the certificate's authority that verified the subject and signed it with its private key.
## Tooling

- `openssl x509 -noout -ext subjectAltName -in <file>` : the SAN of a certificate on disk. Needs OpenSSL. The `openssl` shipped with macOS is LibreSSL 3.3.6 and answers `unknown option -ext`
- `openssl x509 -noout -text` : the portable fallback, the SAN shows up among the extensions
- `openssl s_client -connect <host>:443 -servername <name>` : what the server actually sends, which can differ from what sits on disk
- `curl -w '%{ssl_verify_result}'` : the TLS verdict, read separately from the HTTP code
- `openssl req -in <file>.csr -noout -text | grep -A1 'Subject Alternative Name'` : Read the SAN from a CSR request.

See [[Certificates]], [[X.509]], [[Public Key Infrastructure]], [[Host header]]

## Cards

Q: a client opens `https://www.github.com`. Which field of the certificate decides whether that name is accepted?
A: The SAN field

Q: a certificate has `CN=shop.example.com` and a SAN listing only `DNS:api.example.com`. Which names does it cover?
A: only `api.example.com`. A SAN that is present makes the CN ignored entirely.

Q: why does a root certification authority carry no SAN?
A: because a SAN exists so a client can match the name it asked for against the certificate, and nobody ever matches a hostname against an authority certificate.

Q: the `Subject` field and the SAN both carry names. What is each one for?
A: the `Subject` is a DN naming the entity, and it is the field that chains by equality with the `Issuer` of the level above. The SAN is the list of service names the certificate is valid for, and it is the only one a client matches a requested hostname against.

Q: a certificate is correctly signed, in date, and issued by a trusted authority, and the client still rejects it on the name. Where do you look?
A: the SAN. Signature, dates and chain are a separate set of checks from the name match, so all three can pass while the SAN lists no name you asked for.

Q: a CSR declares a SAN and the issued certificate has none. What happened?
A: `copy_extensions` was left out of the issuing authority's config, so `openssl ca` ignored the request's extensions without saying anything.
