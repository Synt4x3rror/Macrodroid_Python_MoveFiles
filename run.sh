#!/bin/bash

# Declare some variables to hold script path, source directory path and target directory path
script_path=$(wc -l < $1)
source_dir=$(wc -l < $2)
target_dir=$(wc -l < $3)

# Call our python script
python "$script_path" "$source_dir" "$target_dir"