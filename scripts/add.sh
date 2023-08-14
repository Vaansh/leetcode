#!/bin/bash

# Add all changes, staged or unstaged
git add -A

# Get the list of added and modified files
added_files=$(git diff --cached --name-only --diff-filter=A)
modified_files=$(git diff --cached --name-only --diff-filter=M)

# Iterate over added files
for file in $added_files; do
    if [[ $file =~ ^[0-9]+.*\.py$ ]]; then
        if [[ $file =~ ^[0-9]+-.*\.py$ ]]; then
            problem_number=$(echo "$file" | grep -oE '[0-9]+' | head -n 1)
            git commit -m "added solution for problem $problem_number" "$file"
        else
            git commit -m "added file $file" "$file"
            echo "a"
        fi
    fi
done

# Iterate over modified files
for file in $modified_files; do
    if [[ $file =~ ^[0-9]+.*\.py$ ]]; then
        if [[ $file =~ ^[0-9]+-.*\.py$ ]]; then
            problem_number=$(echo "$file" | grep -oE '[0-9]+' | head -n 1)
            git commit -m "updated solution for problem $problem_number" "$file"
        else
            git commit -m "updated file $file" "$file"
            echo "b"
        fi
    fi
done

# Push changes to the remote repository
# git push origin master
