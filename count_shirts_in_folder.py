import datetime
import promptlib
import pandas as pd
import os
from google.oauth2.service_account import Credentials
import pygsheets

today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_root = str(today.year) + "_" + str(today.month)
prompter = promptlib.Files()
path_input = prompter.dir()


def splitted_by_underline(file):
    name, _ = os.path.splitext(file)
    name = name.replace("-", "_")
    split_by_underline = name.split("_")
    splitted = [s.strip() for s in split_by_underline]
    return splitted


class Order:
    def __init__(
        self, date, order_code, side, size, color, set_number, set, seller, product_type
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
    )
    return order


def count_shirts(order):
    variant = (
        order.order_code
        + " - "
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


def count_order(path):
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

        return df[[name, "count"]].drop_duplicates()


def main():
    gc = pygsheets.authorize(
        service_account_file="E:/THANGVT/tools/arranger_v2.2/arrange-PDF-files/luminous-lodge-321503-2defcccdcd2d.json"
    )
    spreadsheet = gc.open_by_key("1iZShXMaHGE_zyHwVkSSfa83dfMpb-qpHHLVXpS7ZxxI")
    worksheet = spreadsheet.worksheet_by_title("Machine 2")
    lst = []
    for root, dirs, files in os.walk(path_input):
        for dir in dirs:
            patho = os.path.join(path_input, dir)
            lst.append(count_order(patho))
    i = 0
    for dtf in lst:
        worksheet.set_dataframe(dtf, start=(3 + i, 1))
        i = i + len(dtf) + 2
    os.system("pause")


main()
