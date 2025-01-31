# docs

Internal Documentation

## Setup / Testing Locally

First, step into a new virtual environment (the second command will differ based on your operating system, this is a good time to read up on virtual environments if you are unfamiliar ;) )

```bash
python -m venv venv
source venv/bin/activate
```

Then, install the dependencies

```bash
pip install -r requirements.txt
```

### Run the local server

```bash
python -m mkdocs serve
```

## Generating PDF of the Consitution

First, follow the steps outlined above to setup the local dev environment.

### Install markdown2, wkhtmltopdf and pdfkit

Download: <https://wkhtmltopdf.org/> (you might need to add it to your path on windows)

### Generate PDF

```bash
python generate_constitution_pdf.py
```
