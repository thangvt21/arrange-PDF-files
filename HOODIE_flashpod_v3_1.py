import os
import shutil
import datetime
import arrow
import promptlib

today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_month = str(today.year) + "_" + str(today.month)
date = str(arrow.now().format("YYYYMMDD"))

prompter = promptlib.Files()

path_input = prompter.dir()

path_P1 = (
    "E:/FlashPOD Dropbox/FlashPOD/Machine 1/" + folder_month + "/" + folder_name + "/"
)
path_P2 = (
    "E:/FlashPOD Dropbox/FlashPOD/Machine 2/" + folder_month + "/" + folder_name + "/"
)
path_P3 = (
    "E:/FlashPOD Dropbox/FlashPOD/Machine 3/" + folder_month + "/" + folder_name + "/"
)
path_P4 = (
    "E:/FlashPOD Dropbox/FlashPOD/Machine 4/" + folder_month + "/" + folder_name + "/"
)
path_P5 = (
    "E:/FlashPOD Dropbox/FlashPOD/Machine 5/" + folder_month + "/" + folder_name + "/"
)
path_P6 = (
    "E:/FlashPOD Dropbox/FlashPOD/Machine 6/" + folder_month + "/" + folder_name + "/"
)

P1 = "TMP_" + date + "_P1_"
P2 = "TMP_" + date + "_P2_"
P3 = "TMP_" + date + "_P3_"
P4 = "TMP_" + date + "_P4_"
P5 = "TMP_" + date + "_P5_"
P6 = "TMP_" + date + "_P6_"

SELF_LABEL = [
    "MERCHFOXSUPPORT",
    "MBTEAM",
    "NGUYENTHUY",
    "SUPPORTTUAN",
    "PHAMPHONGPHU",
    "TDATEAMSUPPORT",
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


def create_path(Order):
    order = Order
    if order.set != "1":
        path = os.path.join(path_P6, P6 + "SET")
    else:
        path = os.path.join(path_P2, P2 + "HOODIE_" + order.color)
    return path


def core():
    list_path = []
    os.chdir(path_input)
    for file in os.listdir():
        order = create_order(file)
        path = create_path(order)
        list_path.append(path)
        try:
            if os.path.exists(path):
                shutil.move(file, path)
            else:
                os.makedirs(path)
                shutil.move(file, path)
        except IndexError as err:
            print("Error: ", err)


def main():
    core()
    os.system("pause")


main()
