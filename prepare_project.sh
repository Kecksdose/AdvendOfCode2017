#!/bin/bash
ID=$1
TEMPLATE="def solve(file):
    with open(file, 'r') as f:


# Test examples
assert solve('test.txt') == 42


# Solve riddle
print(solve('riddle.txt'))
"

if [ "$1" == "" ]; then
    echo "Positional parameter 1 is required"
    exit
fi

mkdir $1

touch "$ID/riddle.txt"
echo $TEMPLATE > "$ID/solution.py"
