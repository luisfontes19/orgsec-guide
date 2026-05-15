# OrgSec Guide

## Introduction

![logo](src/images/banner.png)

This project provides a comprehensive checklist and guide for organizations looking to implement a robust cybersecurity program. Whether you're starting from scratch or looking to enhance your existing security measures, this guide is designed to ensure you cover all essential aspects of organizational cybersecurity.

Check out the project website [here](https://luisfontes19.github.io/orgsec-guide/)

## For local development

Common commands are wrapped in [Taskfile.yml](./Taskfile.yml). Install [Task](https://taskfile.dev/) and run `task` to see the full list.

### Check markdown

```bash
task lint
```

### Fix markdown issues

```bash
task lint:fix
```

### Check markdown links

```bash
task check-links
```

<!-- ### Generate pdf

We use a custom built tool to generate the pdfs called `nicebook`. PDF is generated into the `output` folder.

```bash
chmod +x resources/scripts/generate-pdf.sh
resources/scripts/generate-pdf.sh
``` -->

### Generate and run local website

The `serve` task regenerates the mkdocs nav tree (needed when files are added, removed or renamed) and starts the local server.

```bash
task serve
```

## License

OrgSec Guide © 2025 by Luis Fontes is licensed under CC BY-NC-SA 4.0
