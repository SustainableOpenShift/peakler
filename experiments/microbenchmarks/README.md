# Build

```
COUNT=1 make build/runMEMC

COUNT=5000000 make build/runALU
```

# Grabbing TSC
```
sudo journalctl -k --grep '^tsc:'  | cut -d' ' -f5-
```