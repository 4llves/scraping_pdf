from PrettyColorPrinter import add_printer
from pdferli import get_pdfdf

path=r"D:\Developer\Python\pdfScraping\pdf\NFe02.pdf"

add_printer(1)

df = get_pdfdf(path, normalize_content=False)
print (df)