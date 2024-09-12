#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: ./time_script.sh <python_script> [runs]"
    exit 1
fi

python_script=$1
runs=${2:-5} 

total=0

for i in $(seq 1 $runs); do
    result=$( (time -p python "$python_script") 2>&1 | grep real | awk '{print $2}')
    echo "Run $i: $result seconds"
    total=$(echo "$total + $result" | bc)
done

average=$(echo "$total / $runs" | bc -l)
echo "Average time: $average seconds"
