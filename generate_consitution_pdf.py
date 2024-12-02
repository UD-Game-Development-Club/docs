import markdown2
import pdfkit

def markdown_to_pdf(md_file, pdf_file):
    # Read the Markdown file
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    # Convert Markdown to HTML
    html_content = markdown2.markdown(md_content, extras=["fenced-code-blocks", "tables", "toc"])
    
    css = """
    <style>
        body {
            font-family: 'Times New Roman', Times;
            font-size: 14pt;
            line-height: 1.6;
        }
        h1 {
            font-size: 20pt;
            text-align: left; /* Keep h1 left-aligned */
        }
        h2 { 
            font-size: 18pt; 
            text-align: center; /* Center only h2 headers */
        }
        h3 { 
            font-size: 16pt; 
            text-align: left
        }
        h4, h5, h6 { 
            font-size: 13pt; 
            text-align: left; /* Keep smaller headers left-aligned */
        }
        p, li { 
            margin-bottom: 0.8em; 
        }
    </style>
    """
    html_with_style = f"{css}<body>{html_content}</body>"

    # Convert HTML to PDF
    pdfkit.from_string(html_with_style, pdf_file)
    print(f"PDF generated at: {pdf_file}")

markdown_to_pdf("docs/constitution.md", "gdc_constitution.pdf")