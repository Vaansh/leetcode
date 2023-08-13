#!/bin/bash

echo "number of problems solved: $(($(ls -1 | wc -l) - 2))"
