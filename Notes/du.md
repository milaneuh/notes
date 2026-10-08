---
tags: [linux, tooling]
---
Disk usage inside a path, by walking the tree one entry at a time.

```bash
du -ah /home/example-directory
```

Without `-a`, du only reports directories; `-a` is what adds the individual
files.

See [[df vs du]]
