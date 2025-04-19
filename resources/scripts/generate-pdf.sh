#!/bin/bash

# Uses nicebook to generate a PDF from the markdown files in the src directory

SCRIPT_DIR=$(dirname "$0")
python $SCRIPT_DIR/nicebook_prepare_chapters.py

if [ $? -ne 0 ]; then
    exit 1
fi

pip install nicebook pyyaml

mkdir -p output
root=$(find ./src -maxdepth 1 -type f -name "*.md" ! -name "README.md" | sort)
declare -p root
merged=$(find ./src/checklist -maxdepth 1 -type f -name "*-merged.md" | sort)
nicebook -c resources/nicebook.yml -i "src/README.md" $root src/checklist/checklist.md $merged -o output/orgsec-guide.pdf

rm -f ./src/checklist/*-merged.md
