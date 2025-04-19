# We have one file per item in the checklist, each with a top level heading
# To generate a book we want each file to be a subchapter of the folder it is in
# This script merges all the markdown files in a checklist folder and increases the heading levels by one

import glob
import os
import re

current_path = os.path.dirname(os.path.abspath(__file__))


def get_chapter_title(folder):
    with open(os.path.join(folder, "README.md")) as f:
        content = f.readlines()
        return content[0].strip()


checklist_path = os.path.join(current_path, "..","..", "src", "checklist")
print("Checklist Path: ", checklist_path)

checklist_folders = [d for d in os.listdir(checklist_path) if os.path.isdir(os.path.join(checklist_path, d))]
print("Checklist Folders: ", checklist_folders)

for folder in checklist_folders:

    print("Processing", folder)
    chapter_path = os.path.normpath(os.path.join(checklist_path, folder))

    chapter = get_chapter_title(chapter_path) + "\n\n"

    # Find all files for chapter, sort it alphabetically

    search_pattern = os.path.join(chapter_path, "**", "*.md")
    files = glob.glob(search_pattern, recursive=True)
    files.sort()

    title_regex = r"^(#{1,6})\s+(.*)"

    def replacer(match):
        return '#' + match.group(0)

    for file in files:
        print("  -", file)
        content = open(file).read()

        if file == "README.md":
            # add the file content at the beginning
            chapter = content + chapter + "\n"
        else:
            # Increase the header level
            chapter += re.sub(title_regex, replacer, content, flags=re.MULTILINE)

        chapter += "\n"

    f = os.path.join(os.path.dirname(chapter_path), f"{folder}-merged.md")
    print("Saving file ", f)
    open(f, "w").write(chapter)
