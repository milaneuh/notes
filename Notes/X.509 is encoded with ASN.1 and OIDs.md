---
tags: [pki]
---
**ASN.1** (Abstract Syntax Notation One) defines the datatypes: integers,
strings, sets, sequences, plus object identifiers.

An **OID** tags a value with a type. A string is a string until it carries
`2.5.4.3`, at which point it is a Common Name. That is how a certificate stays
parseable without the parser knowing every field in advance.

See [[X.509]]
