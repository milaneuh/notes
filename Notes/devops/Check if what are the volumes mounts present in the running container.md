To check what are the [[mount point|volume mounts]] currently present in a [[Containers|container]], you can run this command :
```bash
docker inspect mycontainer --format '{{json .Mounts}}' | jq
```
## Cards
Q: how do you list the volume mounts of a running docker container?
A: `docker inspect mycontainer --format '{{json .Mounts}}' | jq`
