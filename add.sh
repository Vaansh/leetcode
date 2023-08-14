#!/bin/bash

# Add all unstaged changes
git add .

# Iterate over added/modified files
git status --porcelain | while read line; do
    status=${line:0:2}
    filename=${line:3}
    
    if [ "$status" == "A " ]; then
        if [[ $filename =~ ^[0-9]+.*\.py$ ]]; then
            # Check if filename starts with a number and ends with .py
            if [[ $filename =~ ^[0-9]+ ]]; then
                problem_number=$(echo "$filename" | grep -oP '^\d+')
                commit_message="added solution for problem $problem_number"
            else
                commit_message="added file: $filename"
            fi
        else
            commit_message="added file: $filename"
        fi
        elif [ "$status" == " M" ]; then
        if [[ $filename =~ ^[0-9]+.*\.py$ ]]; then
            # Check if filename starts with a number and ends with .py
            if [[ $filename =~ ^[0-9]+ ]]; then
                problem_number=$(echo "$filename" | grep -oP '^\d+')
                commit_message="updated solution for problem $problem_number"
            else
                commit_message="updated file: $filename"
            fi
        else
            commit_message="updated file: $filename"
        fi
    fi
    
    # Commit changes with the appropriate message
    git commit -m "$commit_message"
done

# Push changes to the repository
git push
