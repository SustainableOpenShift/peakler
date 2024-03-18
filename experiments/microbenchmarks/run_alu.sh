#!/bin/bash

#set -x

# Script to run build/runALU benchmark
SCRIPT_NAME=$0

# Defaults
NROUNDS=1
NITERS=1
ENDPOINT=""
NPARALLEL=$(nproc)

usage () {
    cat << END_USAGE

${SCRIPT_NAME} - run build/runALU

Usage: ${SCRIPT_NAME} <options>

-n | --nr         : number of rounds for experiment
-i | --it         : iterations to run for runALU
-e | --ep         : endpoint ip:port
-p | --pa         : number of parallel cpus to use
-h | --hp         : usage

END_USAGE

    exit 1
}

# Process command line options. See usage above for supported options
processOptions () {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            -n | --nr)
                NROUNDS="$2"
                shift 2
	    ;;
            -i | --it)
                NITERS="$2"
                shift 2
	    ;;
	    -e | --ep)
		ENDPOINT="$2"
                shift 2
	    ;;
	    -p | --pa)
		NPARALLEL="$2"
                shift 2
	    ;;	    
            -h | --help)
                usage
                exit 0
            ;;
            *)
                usage
            ;;
        esac
    done
}

main () {
    processOptions "$@"

    mkdir -p results
    
    for (( i=0; i<$NROUNDS; i++ )); do
	echo "Round ${i}"
	curl "${ENDPOINT}/metrics" > "results/runALU.nr${i}.it${NITERS}.START"
	sleep 1
	./build/runALU ${NITERS}
	sleep 1
	curl "${ENDPOINT}/metrics" > "results/runALU.nr${i}.it${NITERS}.END"
    done
}

mainParallelk8s () {
    processOptions "$@"

    mkdir -p results

    #NPARALLEL=$(($(nproc)-84))
    NPARALLEL=$(nproc)
    
    ## Warmup run on all the cores
    echo "🟢🟢 Warmup run  🟢🟢"
    for (( j=1; j<=$NPARALLEL; j++ )); do
	taskset -c $(($(nproc)-$j)) ./build/runALU ${NITERS} &
    done
    wait

    # Do actual run
    for (( p=1; p<=$NPARALLEL; p++ )); do
	for (( i=0; i<$NROUNDS; i++ )); do
	    echo "🟢🟢 runALU.ITER${NITERS}.PARALLEL${p}.ROUND${i}.START  🟢🟢"

	    sleep 3	    
	    curl "${ENDPOINT}/metrics" > "results/runALU.ITER${NITERS}.PARALLEL${p}.ROUND${i}.START"
	    
	    for (( j=1; j<=$p; j++ )); do
		taskset -c $(($(nproc)-$j)) ./build/runALU ${NITERS} &
	    done
	    wait
	    sleep 3
	    
	    curl "${ENDPOINT}/metrics" > "results/runALU.ITER${NITERS}.PARALLEL${p}.ROUND${i}.END"
	    echo "🟢🟢 runALU.ITER${NITERS}.PARALLEL${p}.ROUND${i}.END  🟢🟢"
	    echo ""
	    sleep 5
	done
    done
}

runPerfStat() {
    echo $1
    
}

mainParallel () {
    processOptions "$@"
    
    for (( j=1; j<=$NPARALLEL; j++ )); do
	#echo "taskset -c $(($(nproc)-$j)) ./build/runALU ${NITERS} &"
	taskset -c $(($(nproc)-$j)) ./build/runALU ${NITERS} &
    done
    wait
}

single () {
    processOptions "$@"

    # Count down 
    for (( j=0; j<10; j++ )); do
	echo "🟢🟢 Count down $((10-j)) 🟢🟢"
	sleep 1
    done

    echo "taskset -c $(($(nproc)-1)) ./build/runALU ${NITERS}" 
    taskset -c $(($(nproc)-1)) ./build/runALU ${NITERS}

    for (( j=0; j<10; j++ )); do
	echo "🟢🟢 Count down $((10-j)) 🟢🟢"
	sleep 1
    done
}

"$@"
