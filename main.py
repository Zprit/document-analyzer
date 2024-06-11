###Text extraction
# import re #regEx
# from pdfminer.high_level import extract_text, extract_pages

# for page_layout in extract_pages("Gliederung.pdf"):
#     for element in page_layout:
#         print(element)


# text =  extract_text("Gliederung.pdf")

# pattern = re.compile(r"[a-zA-Zöäü]+")
# matches = pattern.findall(text)
# print(matches)


###Image extraction
# import fitz #PyMuPDF
# import PIL.Image #pillow
# import io

# pdf = fitz.open("Sample.pdf")
# counter = 1
# for i in range(len(pdf)):
#     page = pdf[i]
#     images = page.get_images()
#     for image in images:
#         base_img = pdf.extract_image(image[0])
#         image_data = base_img["image"]
#         img = PIL.Image.open(io.BytesIO(image_data))
#         extension = base_img["ext"]
#         img.save(open(f"image{counter}.{extension}", "wb"))
#         counter += 1