#!/bin/bash

set -x

function orig()
{
    NPARALLEL=$(nproc)

    for (( p=1; p<=$NPARALLEL; p++ )); do
	echo "🟢🟢 perf stat -a -e instructions,cache-misses,ref-cycles,power/energy-pkg/,power/energy-ram/ -x, -r 3 -o runALUPerfStat.ITER9000.PARALLEL${p}.REPEAT3 ./run_alu.sh -i 9000 -p $p  🟢🟢"
	sleep 5
	perf stat -a -e instructions,cache-misses,ref-cycles,power/energy-pkg/,power/energy-ram/ -x, -r 3 -o "runALUPerfStat.ITER9000.PARALLEL${p}.REPEAT3" ./run_alu.sh -i 9000 -p $p
	sleep 10
    done
}

function parallel2()
{
    #perf stat -a -e instructions,cache-misses,ref-cycles,power/energy-pkg/,power/energy-ram/ -x, -r 3 ./build/runALU 9000 &
    for (( p=1; p<=3; p++ )); do
	#perf stat -e instructions,cache-misses,cycles taskset -c 1 ./build/runALU 9000 &
	#perf stat -e instructions,cache-misses,cycles taskset -c 7 ./build/runALU 18000 &
	perf stat -a -e power/energy-pkg/,power/energy-ram/ taskset -c 1 ./build/runALU 9000 &
	perf stat -a -e power/energy-pkg/,power/energy-ram/ taskset -c 7 ./build/runALU 18000 &	
	wait
    done
}

"$@"
