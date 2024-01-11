#!/bin/bash

# Directory to search for JSON files
SEARCH_DIR="$1"

# Check if the directory argument is provided and valid
if [[ -z "$SEARCH_DIR" ]]; then
    echo "Usage: $0 <directory>"
    exit 1
elif [ ! -d "$SEARCH_DIR" ]; then
    echo "Error: Directory '$SEARCH_DIR' does not exist."
    exit 1
fi

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "jq is not installed. Please install jq to run this script."
    exit 1
fi

# Function to validate JSON file
validate_json() {
    local file="$1"
    if ! jq empty "$file" > /dev/null 2>&1; then
        echo "Invalid JSON: $file"
    fi
}

# Export the function to use it in the find command
export -f validate_json

# Find and validate all JSON files in the specified directory
find "$SEARCH_DIR" -type f -name "*.json" -exec bash -c 'validate_json "$0"' {} \;

