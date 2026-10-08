---
tags: [linux, systemd]
---
The system and service manager. It describes how to manage each thing on the
machine in a unit file, where a unit is not only a service: there are about a
dozen types, `service`, `timer`, `socket`, `mount`, `target`, `path`.

A unit file is not the configuration of the daemon itself. It is the
description of how systemd should manage it.

See [[Unit files]], [[Active vs Enabled]], [[Diagnosing a systemd service]]
