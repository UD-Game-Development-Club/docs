# docs

Internal Documentation

## Setup / Testing Locally

### Install mkdocs-material

```bash
pip install mkdocs-material
```

### Install mkdocs extensions

```bash
pip install mkdocs-git-revision-date-localized-plugin mkdocs-git-committers-plugin
```

### Run the local server

#### Linux

```bash
mkdocs serve
```

#### Windows

```bash
python -m mkdocs serve
```

## Generating PDF of the Consitution

### Install markdown2, wkhtmltopdf and pdfkit

Download: <https://wkhtmltopdf.org/> (you might need to add it to your path on windows)

```bash
pip install pdfkit markdown2
```

### Generate PDF

```bash
python generate_constitution_pdf.py
```
