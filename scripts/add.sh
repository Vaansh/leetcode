#!/bin/bash

. ./scripts/count.sh
. ./scripts/rename.sh

# rename files
rename "."
rename "java/"

# auto-lint Python files
isort .
black .

# Add all changes, staged or unstaged
git add -A

# Get the list of added, modified, and deleted files
added_files=$(git diff --cached --name-only --diff-filter=A)
modified_files=$(git diff --cached --name-only --diff-filter=M)
deleted_files=$(git diff --cached --name-only --diff-filter=D)

#!/bin/bash

for file in $added_files; do
    file_name=$(basename "$file")
    if [[ $file_name =~ ^[0-9]+-(.*)(\.py|\.java)$ ]]; then
        problem_number=${BASH_REMATCH[1]}
        language_extension=${BASH_REMATCH[2]}
        
        if [ "$language_extension" == ".py" ]; then
            language="python"
        else
            language="java"
        fi
        
        git commit -m "$language: added solution for problem $problem_number" "$file"
    else
        git commit -m "added file $file_name" "$file"
    fi
done

# Iterate over modified files
for file in $modified_files; do
    file_name=$(basename "$file")
    if [[ $file_name =~ ^[0-9]+-(.*)(\.py|\.java)$ ]]; then
        problem_number=${BASH_REMATCH[1]}
        language_extension=${BASH_REMATCH[2]}
        
        if [ "$language_extension" == ".py" ]; then
            language="python"
        else
            language="java"
        fi
        
        git commit -m "$language: updated solution for problem $problem_number" "$file"
    else
        git commit -m "updated file $file_name" "$file"
    fi
done

# Iterate over deleted files
for file in $deleted_files; do
    file_name=$(basename "$file")
    if [[ $file_name =~ ^[0-9]+-(.*)(\.py|\.java)$ ]]; then
        problem_number=${BASH_REMATCH[1]}
        language_extension=${BASH_REMATCH[2]}
        
        if [ "$language_extension" == ".py" ]; then
            language="python"
        else
            language="java"
        fi
        
        git commit -m "$language: deleted solution for problem $problem_number" "$file"
    else
        file_name=$(basename "$file")
        git commit -m "deleted file $file_name" "$file"
    fi
done

# Push changes to the remote repository
git push origin main
