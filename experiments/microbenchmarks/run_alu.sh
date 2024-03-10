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
    
    for (( i=0; i<$NROUNDS; i++ )); do
	echo "Round ${i}"
	curl "${ENDPOINT}/metrics" > "runALU.nr${i}.it${NITERS}.BEGIN"
	sleep 1
	./build/runALU ${NITERS}
	sleep 1
	curl "${ENDPOINT}/metrics" > "runALU.nr${i}.it${NITERS}.END"
    done
}

main "$@"
