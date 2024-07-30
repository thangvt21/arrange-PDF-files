import os
import datetime
from pathlib import PurePath
import promptlib
import pygsheets
import pandas as pd

today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_root = str(today.year) + "_" + str(today.month)

# folder_name = "2024_7_3"
# folder_root = "2024_7"


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
    # name_sheet = str(today.month) + "." + str(today.day)

    MACHINE_LIST = [
        # "PRINTED",
        # "HOTSHOT",
        "Machine 1",
        "Machine 2",
        "Machine 3",
        "Machine 4",
        "Machine 5",
        "Machine 6",
        "Machine 7",
        "Machine 8",
        "Machine 9",
        "Machine 10",
        "Machine 20",
        "Machine 21",
        "Machine 22",
        "Machine 23",
        "Machine 24",
        "Machine 25",
        "Machine 26",
        "Machine 27",
        "Machine 28",
        "Machine 29",
        "Machine 30",
        "Machine 31",
    ]

    i = 1
    for m in MACHINE_LIST:
        root = "D:\\FlashPOD Dropbox\\FlashPOD\\"
        pathR = os.path.join(root, m + "\\" + folder_root + "\\" + folder_name)

        gc = pygsheets.authorize(
            service_account_file="E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\luminous-lodge-321503-2defcccdcd2d.json"
        )
        spreadsheet = gc.open_by_key("1zPjUEOQ8iyHGvL_rfjJWRpAo63hTVKjEx_tCUFFax4k")
        worksheet = spreadsheet.worksheet_by_title("PICK/CUT")

        lst_folder = []
        for root, dirs, files in os.walk(pathR):
            for dir in dirs:
                patho = os.path.join(pathR, dir)
                res = count_order(patho)
                lst_folder.append(res[0])
        df = pd.DataFrame(lst_folder)
        worksheet.set_dataframe(df, start=(2, i), copy_head=False)
        i += 1


main()
