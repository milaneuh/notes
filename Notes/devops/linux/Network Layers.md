 A functioning network includes a set of network layers called a network stack. Every functional network has a stack. The stack looks like this:

1) Application Layer
Contains the "language" applications and servers use to communicate. Usually a high level protocol such as HTTP, TLS or FTP. Application layer protocols can often be combined. For example, TLS combined with HTTP makes HTTPS

2) Transport Layer
Defines the data transmission of the application layer. This layer includes data integrity checks, source and destination ports and specs for breaking application data into packets at the host side. TCP and UDP are the most common layer protocols. The transport layer is sometimes called the protocol layer.

In [[linux]], the transport layer and the layers below it are primarily handled by the linux kernel. But there are exceptions where transport packets are sent to the user space (application layer) for processing.

3) Network layer
Defines how packets from host A can go to host B. The packet transit rule for the internet is called the internet protocol (IP).

4) Physical layer
Defines how to send raw data across a physical medium, such as Ethernet or modem

> [!info] Another way to describe the network layers is the 7-layer OSI model. But since I will primarily be working with the 4 layers seen above, I will not study it for now (Sept 2026).

If you want to send data from host A to host B, the bytes will first leave the application layer on host A and travel through the transport and network layer on host A, then they go down to the physical layer and then up again through the lower layers to the application layer of host B. 

The layers are not completely closed between each other, and sometimes it is more efficient to process them simultaneously. For example, devices that only deal with the physical layer can look at the transport and network layers to filter and route data more quickly. 
## Cards
Q: what is a network stack?
A: the set of network layers a functioning network is built from. Every functional network has one.

Q: what does the application layer define?
A: the "language" applications and servers use to communicate — a high level protocol such as HTTP, TLS or FTP. They can be combined: TLS + HTTP = HTTPS.

Q: what does the transport layer define?
A: the data transmission of the application layer — data integrity checks, source and destination ports, and specs for breaking application data into packets at the host side. TCP and UDP are the most common. Also called the protocol layer.

Q: what does the network layer define?
A: how packets from host A can go to host B. The packet transit rule for the internet is the internet protocol (IP).

Q: what does the physical layer define?
A: how to send raw data across a physical medium, such as Ethernet or modem.

Q: in linux, which layers are handled by the kernel?
A: the transport layer and everything below it, with exceptions where transport packets are sent to user space for processing.

Q: why aren't the network layers completely closed off from each other?
A: because it's sometimes more efficient to process them simultaneously — e.g. devices working at the physical layer can look at the transport and network layers to filter and route data more quickly.
