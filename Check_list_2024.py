import os
import datetime
from pathlib import PurePath
import pygsheets
import pandas as pd

today = datetime.datetime.now()
FOLDER_NAME = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
FOLDER_DIR = str(today.year) + "_" + str(today.month)

# folder_name = "2024_6_2"
# folder_root = "2024_6"

DROPBOX_PATH = "D:\\FlashPOD Dropbox\\FlashPOD\\"
JSON_PATH = (
    "E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\luminous-lodge-321503-2defcccdcd2d.json"
)
SHEET_ID = "1zPjUEOQ8iyHGvL_rfjJWRpAo63hTVKjEx_tCUFFax4k"
MACHINE_LIST = [1,2,3,4,5,6,7,8,9,10,20,21,22,23,24,25,26,27,28,29,30,31]


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
    for _, _, files in os.walk(path):
        list_1 = []
        count_pdf = 0
        name = os.path.basename(path)
        for file in files:
            if file.endswith(".pdf"):
                count_pdf += 1
            splitted = splitted_by_underline(file)
            if splitted[6] != "1":
                order = create_order_set(file)
            else:
                order = create_order(file)
            list_1.append(order.order_code)
            list_ok = list(set(list_1))
        order = len(list_ok)
        return (name, count_pdf, order)


def main():
    while True:
        try:
            set_part = input("Nhap part: ")
            if set_part == "0":
                return
            else:
                tmp = float(set_part)
            break

        except ValueError:
            set_part = input("Nhap part: ")

    name_sheet = FOLDER_NAME + " PART " + str(set_part)

    for m in MACHINE_LIST:
        machine_path = os.path.join(
            DROPBOX_PATH, "Machine" + str(m) + "\\" + FOLDER_DIR + "\\" + FOLDER_NAME
        )
        gc = pygsheets.authorize(service_account_file=JSON_PATH)
        spreadsheet = gc.open_by_key(SHEET_ID)
        worksheet = spreadsheet.worksheet_by_title(m)
        worksheet.clear(start="B5", end="D50")
        worksheet.update_value("B1", name_sheet)
        lst_folder = []
        lst_files = []
        lst_order = []
        for root, dirs, _ in os.walk(machine_path):
            for dir in dirs:
                patho = os.path.join(machine_path, dir)
                res = count_order(patho)
                lst_folder.append(res[0])
                lst_files.append(res[1])
                lst_order.append(res[2])
        df = pd.DataFrame(lst_folder)
        df["1"] = pd.DataFrame(lst_files)
        df["2"] = pd.DataFrame(lst_order)
        worksheet.set_dataframe(df, start=(5, 2), copy_head=False)


main()
