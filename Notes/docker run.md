---
tags: [containers]
---
`docker run --OPTIONS <image> <command>`.

To see what a running container actually got:

```bash
docker inspect mycontainer --format '{{json .Mounts}}' | jq
```

devpod workspaces run docker-outside-of-docker: the workspace talks to the
host's daemon rather than running one of its own.
