A certificate declares the names it is valid for in an X.509v3 extension named `subjectAltName`, the SAN. A TLS client compares the name it was asked to reach against the entries of that list, and rejects the certificate when none of them match.

Entries are typed, and the type is part of the match :

```
X509v3 Subject Alternative Name:
    DNS:github.com, DNS:www.github.com
```

The SAN value type is GeneralName, it can have multiple values but the two that matters for me are. :
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

When the client tries to correlate a CN when a SAN is present in the certificate, then we instead compare to the SAN and we ignore the CN completely. Otherwise, the CN is read.
## The SAN and the Subject field

A root certification authority carries a `Subject` and no SAN at all. The GlobalSign root dumped in [[Certificates]] shows it.

The `Issuer` field identifies the entity that has signed and issued the ceriticate.
> [!todo] à écrire : les deux rôles. Le `Subject` d'une autorité est recopié tel quel dans le champ `Issuer` des certificats qu'elle signe, et c'est cette égalité qui chaîne. Le SAN ne sert qu'à valider le nom demandé. Expliquer pourquoi un certificat serveur au `Subject` vide fonctionne quand même.

## Where the SAN goes missing

> [!todo] à écrire après la construction du cas 2.2 : la CSR porte un SAN, et `openssl x509 -req` l'abandonne en silence sans `-copy_extensions copy`. Le certificat produit est bien signé, dans les dates, et refusé. Noter le message exact rendu par `curl` et celui rendu par `openssl verify`.

## Tooling

- `openssl x509 -noout -ext subjectAltName -in <file>` : the SAN of a certificate on disk. Needs OpenSSL. The `openssl` shipped with macOS is LibreSSL 3.3.6 and answers `unknown option -ext`
- `openssl x509 -noout -text` : the portable fallback, the SAN shows up among the extensions
- `openssl s_client -connect <host>:443 -servername <name>` : what the server actually sends, which can differ from what sits on disk
- `curl -w '%{ssl_verify_result}'` : the TLS verdict, read separately from the HTTP code

> [!todo] à compléter : la commande qui lit le SAN d'une CSR, elle diffère de celle qui lit celui d'un certificat.

See [[Certificates]], [[X.509]], [[Public Key Infrastructure]], [[Host header]]

## Cards

> [!todo] réponses à écrire après la recette du cas 2.2, pas avant.

Q: a client opens `https://www.github.com`. Which field of the certificate decides whether that name is accepted?

Q: a certificate has `CN=shop.example.com` and a SAN listing only `DNS:api.example.com`. Which names does it cover?

Q: why does a root certification authority carry no SAN?

Q: the `Subject` field and the SAN both carry names. What is each one for?

Q: a certificate is correctly signed, in date, and issued by a trusted authority, and the client still rejects it on the name. Where do you look?

Q: a CSR declares a SAN and the issued certificate has none. What happened?
