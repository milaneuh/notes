PKI is the umbrella term for all the practices to issue, distribute, store, use, etc... [[Certificates]] and keys. It's a vague term.

There are a multitude of PKI but the one that I should remember are : 

1. Web PKI
It's sometime called "Internet PKI", they defines what a name is and where it goes in a certificate, what signature algorithms can be used, how a relying party  determines the issuer of a certificate, how certificates validity period is defined, how revocation and certificate path validation works, the process that CAs use to determine  whether or not someone owns a domain and a lot more. 

They are very important because they work by default with browsers and everything else that uses [[TLS]]

2. Internal PKI
You use Internal PKI for services, [[Containers|container]], VMS, hardware,and any other code you need to identify. Contrary to Web PKI, it gives you complete control over details like certificate lifetime, revocation mechanism, renewal processes, key types and algorithms. 

Also, Web PKI can not bind to internal IPs, or internal DNS names that are not resolved in public global DNS. 

See [[Certificates]], [[X.509]]
