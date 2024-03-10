#!/bin/bash

# Script to run build/runALU benchmark
SCRIPT_NAME=$0

# Defaults
NROUNDS=1
NITERS=1
ENDPOINT=""

usage () {
    cat << END_USAGE

${SCRIPT_NAME} - run build/runALU

Usage: ${SCRIPT_NAME} <options>

-n | --nr         : number of rounds for experiment
-i | --it         : iterations to run for runALU
-e | --ep         : endpoint ip:port
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

mainParallel () {
    processOptions "$@"

    mkdir -p results

    #for (( p=1; p<=$(nproc); p++ )); do
    for (( p=1; p<=$(($(nproc)-86)); p++ )); do
	for (( i=0; i<$NROUNDS; i++ )); do
	    echo "Round ${i}"
	    curl "${ENDPOINT}/metrics" > "results/runALU.ITER${NITERS}.PARALLEL${p}.ROUND${i}.START"
	    sleep 1
	    for (( j=1; j<=$p; j++ )); do
		taskset -c $(($(nproc)-$j)) ./build/runALU ${NITERS} &
	    done
	    wait
	    sleep 1
	    curl "${ENDPOINT}/metrics" > "results/runALU.ITER${NITERS}.PARALLEL${p}.ROUND${i}.END"
	    echo "🟢🟢 done runALU.ITER${NITERS}.PARALLEL${p}.ROUND${i}.END 🟢🟢"
	    sleep 5
	done
    done
}

#main "$@"
mainParallel "$@"
