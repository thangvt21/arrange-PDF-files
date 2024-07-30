import datetime
import promptlib
import pandas as pd
import os
from google.oauth2.service_account import Credentials
import pygsheets

today = datetime.datetime.now()
# folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
# folder_root = str(today.year) + "_" + str(today.month)
folder_name = "2024_7_25"
folder_root = "2024_7"


def splitted_by_underline(file):
    name, _ = os.path.splitext(file)
    name = name.replace("-", "_")
    split_by_underline = name.split("_")
    splitted = [s.strip() for s in split_by_underline]
    return splitted


class Order:
    def __init__(
        self,
        date,
        order_code,
        side,
        size,
        color,
        set_number,
        set,
        seller,
        product_type,
        provider,
    ):
        self.date = date
        self.order_code = order_code
        self.side = side
        self.size = size
        self.color = color
        self.set_number = set_number
        self.set = set
        self.seller = seller
        self.product_type = product_type
        self.provider = provider


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
        splitted[9],
        splitted[10],
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
        splitted[9],
        splitted[10],
    )
    return order


def count_shirts(order):
    variant = (
        order.order_code
        + " - "
        + order.provider
        + "/"
        + order.product_type
        + "/"
        + order.color
        + "/"
        + order.size
        + " - "
        + order.set_number
        + "/"
        + order.set
        + " - "
        + order.side
    )
    return variant


def count_list_shirts(path):
    for root, dirs, files in os.walk(path):
        list_var_raw = []
        name = os.path.basename(path)
        for file in files:
            if file.endswith(".pdf"):
                splitted = splitted_by_underline(file)
                if splitted[6] != "1":
                    order = create_order_set(file)
                else:
                    order = create_order(file)
                variant = count_shirts(order)
                list_var_raw.append(variant)
        df = pd.DataFrame([sub.split(" - ") for sub in list_var_raw]).drop_duplicates()
        df["count"] = df[1].map(df[1].value_counts())
        df.columns = ["order_code", name, "set", "side", "count"]
        df.head()
        return df[["order_code", name]].drop_duplicates()


def main():
    MACHINE_LIST = [
        # "PRINTED",
        "HOTSHOT",
        # "Machine 1",
        # "Machine 2",
        # "Machine 3",
        # "Machine 4",
        # "Machine 5",
        # "Machine 6",
        # "Machine 7",
        # "Machine 8",
        # "Machine 9",
        # "Machine 10",
        # "Machine 20",
        # "Machine 21",
        # "Machine 22",
        # "Machine 23",
        # "Machine 24",
        # "Machine 25",
        # "Machine 26",
        # "Machine 27",
    ]

    for m in MACHINE_LIST:
        root = "D:\\FlashPOD Dropbox\\FlashPOD\\"
        pathR = os.path.join(root, m + "\\" + folder_root + "\\" + folder_name)

        gc = pygsheets.authorize(
            service_account_file="E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\luminous-lodge-321503-2defcccdcd2d.json"
        )
        spreadsheet = gc.open_by_key("1iZShXMaHGE_zyHwVkSSfa83dfMpb-qpHHLVXpS7ZxxI")
        worksheet = spreadsheet.worksheet_by_title(m)

        # Xóa ô ngày cũ
        worksheet.clear(start="A1", end="A1")

        # Xóa thống kê áo ngày cũ
        worksheet.clear(start="A3", end="B666")

        # Thêm ô ngày mới
        worksheet.update_value("A1", folder_name)

        lst = []
        for root, dirs, files in os.walk(pathR):
            for dir in dirs:
                patho = os.path.join(pathR, dir)
                lst.append(count_list_shirts(patho))
        i = 0
        for dtf in lst:
            worksheet.set_dataframe(dtf, start=(3 + i, 1))
            i = i + len(dtf) + 2


main()
