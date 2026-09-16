To check what are the [[mount point|volume mounts]] currently present in a [[Containers|container]], you can run this command :
```bash
docker inspect mycontainer --format '{{json .Mounts}}' | jq
```