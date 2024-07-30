import os
import datetime
from pathlib import PurePath
import pygsheets
import pandas as pd

today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_root = str(today.year) + "_" + str(today.month)

# folder_name = "2024_7_3"
# folder_root = "2024_7"

DROPBOX_PATH = "D:\\FlashPOD Dropbox\\FlashPOD\\"
JSON_PATH = (
    "E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\luminous-lodge-321503-2defcccdcd2d.json"
)
SHEET_ID = "1zPjUEOQ8iyHGvL_rfjJWRpAo63hTVKjEx_tCUFFax4k"
MACHINE_LIST = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
]


def splitted_by_underline(file):
    name, _ = os.path.splitext(file)
    name = name.replace("-", "_")
    split_by_underline = name.split("_")
    splitted = [s.strip() for s in split_by_underline]
    return splitted


class Order:
    def __init__(self, date, order_code, side, size, color, set_number, set, seller):
        self.date = date
        self.order_code = order_code
        self.side = side
        self.size = size
        self.color = color
        self.set_number = set_number
        self.set = set
        self.seller = seller


def create_order(file):
    splitted = splitted_by_underline(file)
    order = Order(
        splitted[0],
        splitted[3],
        splitted[4],
        splitted[2],
        splitted[1],
        splitted[5],
        splitted[6],
        splitted[8],
    )
    return order


def create_order_set(file):
    splitted = splitted_by_underline(file)
    order = Order(
        splitted[0],
        splitted[1],
        splitted[4],
        splitted[2],
        splitted[3],
        splitted[5],
        splitted[6],
        splitted[8],
    )
    return order


def count_order(path):
    for root, dirs, files in os.walk(path):
        count_pdf = 0
        name = os.path.basename(path)
        if name[-2] == "_":
            res = name[:-2]
        else:
            res = name[:-3]
        return (res, count_pdf)


def main():
    i = 1
    for m in MACHINE_LIST:
        machine_path = os.path.join(
            DROPBOX_PATH, "Machine " + m + "\\" + folder_root + "\\" + folder_name
        )

        gc = pygsheets.authorize(service_account_file=JSON_PATH)
        spreadsheet = gc.open_by_key(SHEET_ID)
        worksheet = spreadsheet.worksheet_by_title("PICK/CUT")

        lst_folder = []
        for _, dirs, _ in os.walk(machine_path):
            for dir in dirs:
                patho = os.path.join(machine_path, dir)
                res = count_order(patho)
                lst_folder.append(res[0])
        df = pd.DataFrame(lst_folder)
        worksheet.set_dataframe(df, start=(2, i), copy_head=False)
        i += 1


main()
