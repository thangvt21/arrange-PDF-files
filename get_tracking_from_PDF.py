import os
import pytesseract as tess
from PIL import Image
from pdf2image import convert_from_path
import re

PATH_LABEL = r"E:\THANGVT\tools\arranger_v2.2\arrange-PDF-files\download"


def read_pdf(filename):
    pdf_text = ""
    try:
        images = convert_from_path(filename)
        for i, image in enumerate(images):
            name = "page_" + str(i) + "_" + os.path.basename(filename) + ".jpeg"
            image.save(
                "E:/THANGVT/tools/arranger_v2.2/arrange-PDF-files/img/" + name,
                "JPEG",
            )
            tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
            text = tess.image_to_string(
                Image.open(
                    "E:/THANGVT/tools/arranger_v2.2/arrange-PDF-files/img/" + name
                )
            )
            pdf_text = "" + text
            clean_pdf_text = "".join(pdf_text.replace("\n", " "))
            pattern = r"\d{4} \d{4} \d{4} \d{4} \d{4} \d{2}"
            match = re.search(pattern, clean_pdf_text)
            if clean_pdf_text:
                # print(match.group())
                return match.group()
    except Exception as e:
        print(str(e))


for root, dirs, files in os.walk(PATH_LABEL):
    for file in files:
        name, _ = file.split(".pdf")
        path_pdf = PATH_LABEL + "/" + file
        print(read_pdf(path_pdf) + " - " + name)

# path_pdf = "E:/US/PDFFILES/Label/label.pdf"
# read_pdf(path_pdf)
