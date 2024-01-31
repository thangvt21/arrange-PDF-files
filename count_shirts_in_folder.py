import os
import datetime
import promptlib
import pandas as pd

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


def count_shirts(order):
    variant = (
        order.order_code
        + " - "
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
        print(name)
        for file in files:
            if file.endswith(".pdf"):
                splitted = splitted_by_underline(file)
                if splitted[6] != "1":
                    order = create_order_set(file)
                else:
                    order = create_order(file)
                variant = count_shirts(order)
                list_var_raw.append(variant)
        list_res = list(set(list_var_raw))
        count = pd.Series(list_res).value_counts()
        count1 = pd.Series(list_var_raw)
        count2 = count1.drop_duplicates()
        df = pd.DataFrame([sub.split(" - ") for sub in count2])
        count = df[1].value_counts()
        print(count)
        # return name + "-" + str(len(list_ok))
        # print(name + "_" + str(len(list_ok)), list_ok)


def main():
    for root, dirs, files in os.walk(path_input):
        for dir in dirs:
            patho = os.path.join(path_input, dir)
            print(str(count_order(patho)))
    os.system("pause")


main()
