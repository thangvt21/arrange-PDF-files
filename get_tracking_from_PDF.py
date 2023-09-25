import os
import pytesseract as tess
from PIL import Image
from pdf2image import convert_from_path
import re

PATH_LABEL = ""


def read_pdf(filename):
    pages = ""
    try:
        images = convert_from_path(filename)
        for i, image in enumerate(images):
            filename = "page_" + str(i) + "_" + os.path.basename(filename) + ".jpeg"
            image.save(filename, "JPEG")
            tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
            text = tess.image_to_string(Image.open(filename))
            pages = "" + text

    except Exception as e:
        print(str(e))

    clean = "".join(pages.replace("\n", " "))
    # print(clean)
    pattern = r"\d{4} \d{4} \d{4} \d{4} \d{4} \d{2}"
    match = re.search(pattern, clean)
    if pages:
        print(match.group())


pdf_file = "E:/US/TSHIRT/1269 sc 24 pre-paid mailing label 4x6.pdf"
read_pdf(pdf_file)
