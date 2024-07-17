import os
import datetime
from pathlib import PurePath
import promptlib
import pygsheets
import pandas as pd

today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_root = str(today.year) + "_" + str(today.month)

# folder_name = "2024_6_2"
# folder_root = "2024_6"


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

    name_sheet = folder_name + " PART " + str(set_part)

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
    ]

    for m in MACHINE_LIST:
        root = "D:\\FlashPOD Dropbox\\FlashPOD\\"
        pathR = os.path.join(root, m + "\\" + folder_root + "\\" + folder_name)

        gc = pygsheets.authorize(
            service_account_file="E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\luminous-lodge-321503-2defcccdcd2d.json"
        )
        spreadsheet_1stclass = gc.open_by_key(
            "1zPjUEOQ8iyHGvL_rfjJWRpAo63hTVKjEx_tCUFFax4k"
        )
        # spreadsheet_special = gc.open_by_key(
        #     "1Fw5sweTi9vT-CmIr1KYBmqsfz_LJCBPnzCS4Wvo0An0"
        # )
        worksheet_1stclass = spreadsheet_1stclass.worksheet_by_title(m)
        worksheet_1stclass.clear(start="B5", end="D50")
        worksheet_1stclass.update_value("B1", name_sheet)

        # worksheet_special = spreadsheet_special.worksheet_by_title(m)
        # worksheet_special.clear(start="B5", end="D50")
        # worksheet_special.update_value("B1", name_sheet)

        # lst_folder_special = []
        lst_folder_1stclass = []
        lst_files_1stclass = []
        lst_order_1stclass = []
        # lst_order = []
        for root, dirs, files in os.walk(pathR):
            for dir in dirs:
                patho = os.path.join(pathR, dir)
                res = count_order(patho)
                # test = res[0]
                # test1 = test[:6]
                # if test1[-3:] == "24H" or test1[-3:] == "EX_" or test1[-3:] == "CAR":
                # lst_folder_special.append(res[0])
                # else:
                lst_folder_1stclass.append(res[0])
                lst_files_1stclass.append(res[1])
                lst_order_1stclass.append(res[2])
        # df_special = pd.DataFrame(lst_folder_special)
        df_1stclass = pd.DataFrame(lst_folder_1stclass)
        df_1stclass["1"] = pd.DataFrame(lst_files_1stclass)
        df_1stclass["2"] = pd.DataFrame(lst_order_1stclass)
        # worksheet_special.set_dataframe(df_special, start=(5, 2), copy_head=False)
        worksheet_1stclass.set_dataframe(df_1stclass, start=(5, 2), copy_head=False)


main()
