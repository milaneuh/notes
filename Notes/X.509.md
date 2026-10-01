Standardized digital document to bind a public key to an identity, using a digital signature from a trusted third party (_issuer_). It forms the foundation of [[Public Key Infrastructure|PKI]]. 

It was first standardized in 1988 as part of the broader X.500 project, a project created by the telcos to build a global telephone book. This is why you can find the locality, state and country in a x.509 certificate. 

`Subject: C=BE, O=GlobalSign nv-sa, CN=GlobalSign Root R46`

It is built on top of _ASN.1_ (Abstract Syntax Notation One), it defines the datatypes. It has normal datatypes such as integer, strings, set and sequences. It also has unusual type that's important to understand: object identifiers (OID). OID are used to tag a bit of data with a type. A string is just a string, but if I tag it with a OID of `2.5.4.3` then it's no longer a string, it's a X.509 common name

`Subject: C=BE, O=GlobalSign nv-sa, CN=GlobalSign Root R46`

OID 2.5.4.3 (DN component CommonName)= GlobalSign Root R46

See [[Certificates]], [[Public Key Infrastructure]], [[Subject Alternative Name]]
