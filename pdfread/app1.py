
from PyPDF2 import PdfReader

# 1
pdf_reader = PdfReader("C:/Users/E-IACOSTA/Desktop/pdfread/SINIESTRO.pdf")
#output_file_path = Path.home() / "C:\UsersxFinn\Documents\Pollo\Backup Pollo\POLLO TRABAJO GENTERA\Programas\SixSigma-Garciacano-Gabriel.txt"
output_file_path = "C:/Users/E-IACOSTA/Desktop/pdfread"
# 2

with open(output_file_path, mode="w", encoding="utf8") as output_file:
    # 3
    title = pdf_reader.metadata.title
    num_pages = len(pdf_reader.pages)
    print(len(pdf_reader.pages))
    output_file.write(f"{title}\nNumber of pages: {num_pages}\n\n")

    # 4
    for page in pdf_reader.pages:
        text = page.extract_text()
        print(text)
        output_file.write(text)