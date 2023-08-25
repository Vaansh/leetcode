#!/bin/bash

rename() {
    for filename in "$1"/*; do
        if [ -f "$filename" ]; then
            match=$(echo "$filename" | grep -oE '([0-9]+)\. (.+)')
            if [ ! -z "$match" ]; then
                number=$(echo "$match" | sed -E 's/([0-9]+)\. (.+)/\1/' | printf "%04d" "$(cat -)")
                title=$(echo "$match" | sed -E 's/([0-9]+)\. (.+)/\2/' | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | tr -d '.')
                
                # Check if the file is in the "java/" folder
                if [[ "$filename" == *"java/"* ]]; then
                    new_extension=".java"
                else
                    new_extension=".py"
                fi
                
                new_filename="${number}-${title}${new_extension}"
                mv "$filename" "$1/$new_filename"
                echo "Renamed '$filename' to '$new_filename'"
            fi
        fi
    done
}
