#!/bin/bash

count() {
    python_count=$(find ./python -type f -name "*.py" | wc -l)
    java_count=$(find ./java -type f -name "*.java" | wc -l)
    
    # Construct the updated table with Markdown formatting
    updated_table="<!-- SOLUTIONS_START -->
    
    <table style='width:100%; text-align:left;'>
    <tr>
    <th style='text-align:center;'>Language</th>
    <th style='text-align:center;'>Number of Solutions</th>
    </tr>
    <tr>
    <td>Python</td>
    <td>$python_count</td>
    </tr>
    <tr>
    <td>Java</td>
    <td>$java_count</td>
    </tr>
    </table>
    
    <!-- SOLUTIONS_END -->"
    
    # Read the README.md contents
    readme_contents=$(cat README.md)
    
    # Replace the section between <!-- SOLUTIONS_START --> and <!-- SOLUTIONS_END -->
    updated_readme="${readme_contents/<!-- SOLUTIONS_START -->[^<]*<!-- SOLUTIONS_END -->/$updated_table}"
    
    # Write the updated content back to README.md
    echo "$updated_readme" > README.md
    
    echo "Number of solutions solved:"
    echo "------------------------------"
    printf "%-10s %s\n" "Language" "Number of Solutions"
    echo "------------------------------"
    printf "%-10s %d\n" "Python" $python_count
    printf "%-10s %d\n" "Java" $java_count
    echo "------------------------------"
}