Standardized digital document to bind a public key to an identity, using a digital signature from a trusted third party (_issuer_). It forms the foundation of [[Public Key Infrastructure|PKI]]. 

It was first standardized in 1988 as part of the broader X.500 project, a project created by the telcos to build a global telephone book. This is why you can find the locality, state and country in a x.509 certificate. 

`Subject: C=BE, O=GlobalSign nv-sa, CN=GlobalSign Root R46`

It is built on top of _ASN.1_ (Abstract Syntax Notation One), it defines the datatypes. It has normal datatypes such as integer, strings, set and sequences. It also has unusual type that's important to understand: object identifiers (OID). OID are used to tag a bit of data with a type. A string is just a string, but if I tag it with a OID of `2.5.4.3` then it's no longer a string, it's a X.509 common name

`Subject: C=BE, O=GlobalSign nv-sa, CN=GlobalSign Root R46`

OID 2.5.4.3 (DN component CommonName)= GlobalSign Root R46

See [[Certificates]], [[Public Key Infrastructure]], [[Subject Alternative Name]]

## Cards
Q: why does an X.509 certificate carry a locality, a state and a country?
A: it comes from X.500, a 1988 telco project to build a global telephone book, and those fields were kept.

Q: what is ASN.1, and what does it provide to X.509?
A: Abstract Syntax Notation One. It defines the datatypes a certificate is built from, integers, strings, sets and sequences.

Q: what does an OID do to a piece of data?
A: it tags it with a type. The same string tagged `2.5.4.3` stops being a string and becomes a Common Name.

Q: a certificate binds a public key to an identity. What makes that binding worth anything?
A: a digital signature from the issuer.
