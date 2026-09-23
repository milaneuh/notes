In linux, a loopback (lo) is a special virtual interface that lets your computer talk to itself. It uses the IP address 127.0.0.1 and is vital for local network testing, services and internal communication. 

See: 
	-[[network loopback]]
	-[[file loopback]]
	-[[audio loopback]]

## Cards
Q: what does the loopback interface carry?
A: traffic from the host to itself. A packet on `lo` never reaches the network.

Q: a service is bound and answers locally, but nothing reaches it from another machine. First hypothesis?
A: it is bound on loopback, so only the host itself can reach it.
