#!/bin/bash

rename() {
    for filename in "$1"/*; do
        if [ -f "$filename" ]; then
            match=$(echo "$filename" | grep -oE '([0-9]+)\. (.+)')
            if [ ! -z "$match" ]; then
                number=$(echo "$match" | sed -E 's/([0-9]+)\. (.+)/\1/' | printf "%04d" "$(cat -)")
                title=$(echo "$match" | sed -E 's/([0-9]+)\. (.+)/\2/' | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | tr -d '.')
                new_filename="${number}-${title}.py"
                mv "$filename" "$1/$new_filename"
                echo "Renamed '$filename' to '$new_filename'"
            fi
        fi
    done
}
