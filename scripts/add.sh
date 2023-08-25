#!/bin/bash

. ./scripts/count.sh
. ./scripts/rename.sh

# rename files
rename "python/"
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
moved_files=$(git diff --cached --name-only --diff-filter=R)

# Iterate over added files
for file in $added_files; do
    file_name=$(basename "$file")
    if [[ $file_name =~ ^[0-9]+-(.*)(\.py|\.java)$ ]]; then
        problem_number=$(echo "$file_name" | grep -oE '[0-9]+' | head -n 1)
        language_extension=$(echo "$file_name" | grep -oE '\.(java|py)$')
        
        case $language_extension in
            .py) language="python" ;;
            .java) language="java" ;;
            *) language="unknown" ;;
        esac
        
        git commit -m "$language: added solution for problem $problem_number" "$file"
    else
        git commit -m "added file $file_name" "$file"
    fi
done


# Iterate over modified files
for file in $modified_files; do
    file_name=$(basename "$file")
    if [[ $file_name =~ ^[0-9]+-(.*)(\.py|\.java)$ ]]; then
        problem_number=$(echo "$file_name" | grep -oE '[0-9]+' | head -n 1)
        language_extension=$(echo "$file_name" | grep -oE '\.(java|py)$')
        
        case $language_extension in
            .py) language="python" ;;
            .java) language="java" ;;
            *) language="unknown" ;;
        esac
        
        git commit -m "$language: updated solution for problem $problem_number" "$file"
    else
        file_name=$(basename "$file")
        git commit -m "updated file $file_name" "$file"
    fi
done

# Iterate over deleted files
for file in $deleted_files; do
    file_name=$(basename "$file")
    if [[ $file_name =~ ^[0-9]+-(.*)(\.py|\.java)$ ]]; then
        problem_number=$(echo "$file_name" | grep -oE '[0-9]+' | head -n 1)
        language_extension=$(echo "$file_name" | grep -oE '\.(java|py)$')
        
        case $language_extension in
            .py) language="python" ;;
            .java) language="java" ;;
            *) language="unknown" ;;
        esac
        
        git commit -m "$language: deleted solution for problem $problem_number" "$file"
    else
        file_name=$(basename "$file")
        git commit -m "deleted file $file_name" "$file"
    fi
done

# Iterate over moved files
for file in $moved_files; do
    file_name=$(basename "$file")
    if [[ $file_name =~ ^[0-9]+-(.*)(\.py|\.java)$ ]]; then
        problem_number=$(echo "$file_name" | grep -oE '[0-9]+' | head -n 1)
        language_extension=$(echo "$file_name" | grep -oE '\.(java|py)$')
        
        case $language_extension in
            .py) language="python" ;;
            .java) language="java" ;;
            *) language="unknown" ;;
        esac
        
        git commit -m "$language: moved solution for problem $problem_number" "$file"
    else
        file_name=$(basename "$file")
        git commit -m "moved file $file_name" "$file"
    fi
done

# Push changes to the remote repository
# echo push origin main
