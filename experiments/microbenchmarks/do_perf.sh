#!/bin/bash

NPARALLEL=$(nproc)

for (( p=1; p<=$NPARALLEL; p++ )); do
    echo "🟢🟢 perf stat -a -e instructions,cache-misses,ref-cycles,power/energy-pkg/,power/energy-ram/ -x, -r 3 -o runALUPerfStat.ITER9000.PARALLEL${p}.REPEAT3 ./run_alu.sh -i 9000 -p $p  🟢🟢"
    sleep 5
    perf stat -a -e instructions,cache-misses,ref-cycles,power/energy-pkg/,power/energy-ram/ -x, -r 3 -o "runALUPerfStat.ITER9000.PARALLEL${p}.REPEAT3" ./run_alu.sh -i 9000 -p $p
    sleep 10
done
