import os
import yaml

# Prepare the navigation tree for mkdocs. This tree is configured in mkfile_path
# This script reads the src folder and generates the tree based on the file structure in there.
# Readme files are treated as index files

current_path = os.path.dirname(os.path.abspath(__file__))
root_folder = os.path.join(current_path, "..", "..")
src_folder = os.path.join(root_folder, "src")
mkfile_path = os.path.join(root_folder,"resources", "mkdocs.yml")
checklist_path = os.path.join(src_folder, "checklist")

def checklist_chapters() -> dict:
    chapters = os.listdir(checklist_path)
    chapters.sort()
    ret = {}

    for c in chapters:
        # if not file
        if not os.path.isdir(os.path.join(checklist_path, c)):
            continue

        readme = os.path.join(checklist_path, c, "README.md")

        with open(readme) as file:
            ret[c] = file.readline().replace("# ", "").strip()

    return ret


mkdocs_content = {}

with open(mkfile_path, "r") as mkfile:

    mkdocs_content = yaml.safe_load(mkfile)
    mkdocs_content["nav"] = []
    src_files = [d for d in sorted(os.listdir(src_folder))]

    mkdocs_content["nav"].append({"Home": "README.md"})

    # Each file in the src folder
    for file in src_files:
        if not file.endswith(".md"):
            continue

        if file == "README.md":
            continue

        f_path = os.path.join(src_folder, file)
        with open(f_path) as f:
            content = f.read()
            if content.startswith("# "):
                title = content.split("\n")[0].replace("# ", "")
                mkdocs_content["nav"].append({title: file})


    chapters = checklist_chapters()
    mkdocs_content["nav"].append({"Checklist": "checklist/checklist.md"})
    chapters_sections = []

    # for each chapter
    for file, chapter in chapters.items():
        chapter_folder = os.path.join(src_folder, "checklist", file)
        chapter_files = [d for d in sorted(os.listdir(chapter_folder))]

        mkdoc_chapter_obj = []

        # Each file in the chapter folder
        for c_file in chapter_files:
            if not c_file.endswith(".md"):
                continue

            if c_file == "README.md":
                mkdoc_chapter_obj.append({"Home": f'checklist/{file}/{c_file}'})
                continue

            # Get the title of the file
            with open(os.path.join(chapter_folder, c_file)) as f:
                content = f.read()
                if content.startswith("# "):
                    title = content.split("\n")[0].replace("# ", "")
                    mkdoc_chapter_obj.append({title: f'checklist/{file}/{c_file}'})


        mkdocs_content["nav"].append({chapter: mkdoc_chapter_obj})

with open(mkfile_path, "w") as mkfile:
    yaml.dump(mkdocs_content, mkfile,  sort_keys=False,  # Keeps keys in original order
        allow_unicode=True)

