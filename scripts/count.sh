#!/bin/bash

python_count=$(find ./python -type f -name "*.py" | wc -l)
java_count=$(find ./java -type f -name "*.java" | wc -l)

echo "Number of solutions solved:"
echo "------------------------------"
printf "%-10s %s\n" "Language" "Number of Solutions"
echo "------------------------------"
printf "%-10s %d\n" "Python" $python_count
printf "%-10s %d\n" "Java" $java_count
echo "------------------------------"
