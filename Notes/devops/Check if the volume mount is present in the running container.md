```bash
docker inspect mycontainer --format '{{json .Mounts}}' | jq
```