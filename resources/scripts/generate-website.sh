# Uses mkdocs to generate a website from the markdown files in the src directory

SCRIPT_DIR=$(dirname "$0")
chmod +x $SCRIPT_DIR/nicebook_prepare_chapters.py
mkdocs gh-deploy -d output/site -f resources/mkdocs.yml --force
