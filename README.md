# OrgSec Guide

## Introduction

![logo](src/images/banner.png)

This project provides a comprehensive checklist and guide for organizations looking to implement a robust cybersecurity program. Whether you're starting from scratch or looking to enhance your existing security measures, this guide is designed to ensure you cover all essential aspects of organizational cybersecurity.

## Usage

### Check markdown

```bash
markdownlint-cli2 "src/**/*.md"
```

### Fix markdown issues

```bash
markdownlint-cli2 "src/**/*.md" --fix
```

### Check markdown links

```bash
chmod +x resources/scripts/check-links.sh
resources/scripts/check-links.sh
```

### Generate pdf

We use a custom built tool to generate the pdfs called `nicebook`. PDF is generated into the `output` folder.

```bash
chmod +x resources/scripts/generate-pdf.sh
resources/scripts/generate-pdf.sh
```

### Generate and run local website

```bash
chmod +x resources/scripts/mkdocs-config.sh

## This file will generate the tree, so if you change file names or locations or add/remove files you may want to run this script again
./resources/scripts/mkdocs-config.sh
mkdocs serve -f resources/mkdocs.yml  -w src
```

## License

OrgSec Guide © 2025 by Luis Fontes is licensed under CC BY-NC-SA 4.0
