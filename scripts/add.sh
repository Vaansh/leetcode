#!/bin/bash

. ./scripts/count.sh
. ./scripts/rename.sh

# rename files
rename "."

# lint files
isort .
black .

# Add all changes, staged or unstaged
git add -A

# Get the list of added, modified, and deleted files
added_files=$(git diff --cached --name-only --diff-filter=A)
modified_files=$(git diff --cached --name-only --diff-filter=M)
deleted_files=$(git diff --cached --name-only --diff-filter=D)

# Iterate over added files
for file in $added_files; do
    if [[ $file =~ ^[0-9]+-.*\.py$ ]]; then
        file_name=$(basename "$file")
        problem_number=$(echo "$file_name" | grep -oE '[0-9]+' | head -n 1)
        git commit -m "added solution for problem $problem_number" "$file"
    else
        file_name=$(basename "$file")
        git commit -m "added file $file_name" "$file"
    fi
done

# Iterate over modified files
for file in $modified_files; do
    if [[ $file =~ ^[0-9]+-.*\.py$ ]]; then
        file_name=$(basename "$file")
        problem_number=$(echo "$file_name" | grep -oE '[0-9]+' | head -n 1)
        git commit -m "updated solution for problem $problem_number" "$file"
    else
        file_name=$(basename "$file")
        git commit -m "updated file $file_name" "$file"
    fi
done

# Iterate over deleted files
for file in $deleted_files; do
    if [[ $file =~ ^[0-9]+-.*\.py$ ]]; then
        file_name=$(basename "$file")
        problem_number=$(echo "$file_name" | grep -oE '[0-9]+' | head -n 1)
        git commit -m "deleted solution for problem $problem_number" "$file"
    else
        file_name=$(basename "$file")
        git commit -m "deleted file $file_name" "$file"
    fi
done

# Push changes to the remote repository
git push origin main
