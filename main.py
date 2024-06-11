import re #regEx
from pdfminer.high_level import extract_text, extract_pages

# for page_layout in extract_pages("Gliederung.pdf"):
#     for element in page_layout:
#         print(element)


text =  extract_text("Gliederung.pdf")

pattern = re.compile(r"[a-zA-Z]+")
matches = pattern.findall(text)
print(matches)