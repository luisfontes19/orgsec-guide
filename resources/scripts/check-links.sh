# Check if links referenced in the markdown files are valid and active

npm install -g markdown-link-check

find src -type f -name '*.md' | while read file; do
    markdown-link-check -c .markdownlink.json $file
done
