PKI is the umbrella term for all the practices to issue, distribute, store, use, etc... [[Certificates]] and keys. It's a vague term.

There are a multitude of PKI but the one that I should remember are : 

1. Web PKI
It's sometime called "Internet PKI", they defines what a name is and where it goes in a certificate, what signature algorithms can be used, how a relying party  determines the issuer of a certificate, how certificates validity period is defined, how revocation and certificate path validation works, the process that CAs use to determine  whether or not someone owns a domain and a lot more. 

They are very important because they work by default with browsers and everything else that uses [[TLS]]

2. Internal PKI
You use Internal PKI for services, [[Containers|container]], VMS, hardware,and any other code you need to identify. Contrary to Web PKI, it gives you complete control over details like certificate lifetime, revocation mechanism, renewal processes, key types and algorithms. 

Also, Web PKI can not bind to internal IPs, or internal DNS names that are not resolved in public global DNS. 

See [[Certificates]], [[X.509]]

## Cards
Q: what does PKI cover?
A: the practices around issuing, distributing, storing and using certificates and keys. The term is vague on purpose.

Q: what does Web PKI give you for free, and what does it take from you in exchange?
A: it works by default in browsers and in anything using TLS. In exchange it fixes the name rules, the algorithms, the validity periods, the revocation mechanism and the path validation.

Q: what does an internal PKI let you control that Web PKI does not?
A: certificate lifetime, revocation mechanism, renewal process, key types and algorithms.

Q: you need a certificate for an internal IP, or for a DNS name that does not resolve publicly. Why can Web PKI not help?
A: it cannot bind a name it has no way to verify, so it will not issue for names absent from the global DNS.
