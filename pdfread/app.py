from pathlib import Path
from PyPDF2 import PdfReader

# Change the path below to the correct path for your computer.
pdf_path = (
    Path.home() / "C:/Users/E-IACOSTA/Desktop/pdfread/SINIESTRO.pdf"
)

# 1
pdf_reader = PdfReader(str(pdf_path))
output_file_path = Path.home() / "C:/Users/E-IACOSTA/Desktop/pdfreadPrid.txt"

# 2
with output_file_path.open(mode="w") as output_file:
    # 3
    title = pdf_reader.metadata.title
    num_pages = len(pdf_reader.pages)
    output_file.write(f"{title}\\nNumber of pages: {num_pages}\\n\\n")

    # 4
    for page in pdf_reader.pages:
        text = page. extract_text()
        output_file.write(text)

print(text)