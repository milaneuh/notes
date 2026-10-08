---
tags: [networking]
---
A functioning network is a stack of layers:

1. **Application**: the language two programs speak, HTTP, TLS, FTP. They
   combine, TLS over HTTP is HTTPS.
2. **[[Transport layer]]**: ports, integrity checks, cutting application data
   into packets. TCP and UDP.
3. **[[Network layer]]**: how a packet gets from host A to host B, regardless
   of hardware or OS. IP.
4. **[[Physical layer]]**: raw data over a medium, ethernet, wireless, modem.

In linux the kernel handles the transport layer and everything below, with
exceptions where transport packets are handed to user space.

The layers are not closed off from each other: a router can read the transport
port to filter while routing on the network layer, because that is faster.

Diagnostically, if two hosts ping but the application cannot connect, the
network layer and below work, and the fault is in transport or application.
