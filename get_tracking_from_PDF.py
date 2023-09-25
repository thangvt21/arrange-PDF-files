import os
import pytesseract as tess
from PIL import Image
from pdf2image import convert_from_path


def read_pdf(filename):
    pages = []
    try:
        images = convert_from_path(filename)
        for i, image in enumerate(images):
            filename = "page_" + str(i) + "_" + os.path.basename(filename) + ".jpeg"
            image.save(filename, "JPEG")
            tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
            text = tess.image_to_string(Image.open(filename))
            pages.append(text)

    except Exception as e:
        print(str(e))

    output_filename = os.path.splitext(filename)[0] + ".txt"
    with open(output_filename, "w") as f:
        f.write("\n".join(pages))
    return output_filename


pdf_file = "E:/US/TSHIRT/1269 sc 24 pre-paid mailing label 4x6.pdf"
print(read_pdf(pdf_file))
