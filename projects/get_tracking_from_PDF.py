import os
import pytesseract as tess
from PIL import Image
from pdf2image import convert_from_path
import re
import promptlib

prompter = promptlib.Files()

PATH_LABEL = prompter.dir()
PATH_IMAGE = "E:/THANGVT/vtt_tools/arrange-PDF-files/img/7.22/"


def read_pdf(filename: str):
    
    try:
        images = convert_from_path(filename)
        for i, image in enumerate(images):
            img_name = "page_" + str(i) + "_" + os.path.basename(filename) + ".jpeg"
            image.save(
                PATH_IMAGE + img_name,
                "JPEG",
            )
            tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
            text = tess.image_to_string(Image.open(PATH_IMAGE + img_name))
            pdf_text = "" + text
            clean_pdf_text = "".join(pdf_text.replace("\n", " "))
            pattern = r"\d{4} \d{4} \d{4} \d{4} \d{4} \d{2}"
            pattern1 = r"\d{4} \d{4} \d{4} \d{4} \d{4} \d{4} \d{2}"
            match = re.search(pattern1, clean_pdf_text)
            try:
                if match:
                    return match.group()
                else:
                    match = re.search(pattern, clean_pdf_text)
                    if match:
                        return match.group()
            except:
                print("Error: ", IndexError)
    except Exception as e:
        print(str(e))


for root, dirs, files in os.walk(PATH_LABEL):
    for file in files:
        name = file.split(".pdf")
        path_pdf = PATH_LABEL + "/" + file
        print(str(read_pdf(path_pdf)) + " - " + name[0])
