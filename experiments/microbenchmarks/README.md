# Build

```
COUNT=1 make build/runMEMC

COUNT=5000000 make build/runALU

# This has uses custom pcm library that reads from MSR registers directly
COUNT=5000000 make build/runALUpcm 
```

# Grabbing TSC
```
sudo journalctl -k --grep '^tsc:'  | cut -d' ' -f5-
```