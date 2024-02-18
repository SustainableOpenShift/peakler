#!/bin/bash
if [[ $# -lt 4 ]]; then
 echo "Usage: $0 <duration> <increment> <iterations> <cpu-method> [num_procs]"
 exit 1
fi

num_procs=64
duration=$1
increment=$2
iterations=$3
method=$4
if [ ! -z $5 ]
then
    num_procs=$5
fi

echo $num_procs

#date +%s >> $reftimefile
for (( iter=0; iter<$iterations; iter++)); do
  for (( i=1; i<=$num_procs; i+=2 )); do
    this_procs=$(( $RANDOM % $num_procs + 1 ))
    echo $this_procs
    stress-ng --cpu $this_procs --cpu-method $method -t ${duration}s
    echo "sleep $(( 2 * ( this_procs / 10 + 1 )))"
    
    sleep $(( 2 * ( this_procs / 10 + 1 )))
    echo
  done
  echo
done
