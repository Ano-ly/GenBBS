#!/bin/bash

# Directory containing .ui files
UI_DIR="assets/ui"

# Output directory for Python UI files
OUTPUT_DIR="src/gui"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop through all .ui files in the UI_DIR
for ui_file in "$UI_DIR"/*.ui;
do
    # Extract the base name of the file (e.g., GenBBS_loading.ui -> GenBBS_loading)
    base_name=$(basename "$ui_file" .ui)
    
    # Define the output Python file name (e.g., ui_GenBBS_loading.py)
    output_file="$OUTPUT_DIR"/ui_"$base_name".py
    
    echo "Compiling $ui_file to $output_file"
    
    # Use pyside6-uic to convert the .ui file to a Python file
    pyside6-uic "$ui_file" -o "$output_file"
done

echo "UI compilation complete."