#!/bin/bash

# Script to prepare for mkdocs usage

pip install mkdocs mkdocs-material tzdata pytz mkdocs-rss-plugin
mkdir -p output/site

SCRIPT_DIR=$(dirname "$0")
python $SCRIPT_DIR/mkdocs_prepare_tree.py
