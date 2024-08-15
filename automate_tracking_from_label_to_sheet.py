import os
import pytesseract as tess
from PIL import Image
from pdf2image import convert_from_path
import re
import pygsheets
import requests

# import logging


# logging.basicConfig(
#     level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
# )
SHEET_ID = "1lX8xs3zJVinhRs_r4itv6V8gAw4Aut8rY_waj3LHql4"
JSON_PATH = (
    "E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\luminous-lodge-321503-2defcccdcd2d.json"
)
PATH_IMAGE = "E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\img\\"

TRACKING_22 = r"\d{4} \d{4} \d{4} \d{4} \d{4} \d{2}"
TRACKING_26 = r"\d{4} \d{4} \d{4} \d{4} \d{4} \d{4} \d{2}"


""" TO DO:
    Download tesseract, install it and copy path to TESSERACT_PATH:
    https://github.com/tesseract-ocr/tesseract/releases

    Download poppler, and add path/to/bin to Environment Variables:
    https://github.com/oschwartz10612/poppler-windows/releases
"""

TESSERACT_PATH = "C:\\Program Files\\Tesseract-OCR\\tesseract"


def connect_to_sheet(sheet_id: str):
    sheet_name = input("Tên sheet: ")
    gc = pygsheets.authorize(service_account_file=JSON_PATH)
    spreadsheet = gc.open_by_key(sheet_id)
    worksheet = spreadsheet.worksheet_by_title(sheet_name.strip())
    return worksheet


def ocr_pdf_and_find_text(filename: str):
    # logging.debug("Start OCR (%s)" % (filename))
    try:
        images = convert_from_path(filename)
        for i, image in enumerate(images):
            name = str(i) + "_" + os.path.basename(filename) + ".jpeg"
            image.save(
                PATH_IMAGE + name,
                "JPEG",
            )
            tess.pytesseract.tesseract_cmd = TESSERACT_PATH
            text = tess.image_to_string(Image.open(PATH_IMAGE + name))
            pdf_text = "" + text
            clean_pdf_text = "".join(pdf_text.replace("\n", " "))
            match = re.search(TRACKING_26, clean_pdf_text)
            try:
                if match:
                    return match.group()
                else:
                    match = re.search(TRACKING_22, clean_pdf_text)
                    if match:
                        return match.group()
            except:
                print("Error: ", IndexError)
    except Exception as e:
        print(str(e))


def convert_drive_link(drive_link: str):
    try:
        file_id = drive_link.split("/d/")[1].split("/")[0]
        return f"https://drive.google.com/uc?id={file_id}"
    except IndexError:
        return None


def main():
    worksheet = connect_to_sheet(SHEET_ID)
    a = worksheet.get_all_values(
        returnas="matrix",
        majdim="rows",
        include_tailing_empty=False,
        include_tailing_empty_rows=False,
    )
    for i, v in enumerate(a, start=1):
        if v:
            output_path = os.path.join(PATH_IMAGE, f"{v[0]}.pdf")
            url = convert_drive_link(v[3])
            if url:
                with requests.get(url, stream=True) as r:
                    r.raise_for_status()
                    with open(output_path, "wb") as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
                data = ocr_pdf_and_find_text(output_path)
                value = str(data).replace(" ", "")
                worksheet.update_value(f"E{i}", value, parse=True)


main()
