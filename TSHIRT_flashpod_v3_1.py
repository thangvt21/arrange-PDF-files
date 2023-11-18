import os
import shutil
import datetime
import arrow
import promptlib


today = datetime.datetime.now()
date = str(arrow.now().format("YYYYMMDD"))

folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_month = str(today.year) + "_" + str(today.month)

# path = "E:/FlashPOD Dropbox/Thang Vo/7_TrungDH/18.11.2023/Done/18_2_hoodie_184_A Trung"

# path_input = path.replace("''", "/")

prompter = promptlib.Files()

path_input = prompter.dir()

# path_P1 = (
#     "E:/FlashPOD Dropbox/FlashPOD/Machine 1/" + folder_month + "/" + folder_name + "/"
# )
# path_P2 = (
#     "E:/FlashPOD Dropbox/FlashPOD/Machine 2/" + folder_month + "/" + folder_name + "/"
# )
# path_P3 = (
#     "E:/FlashPOD Dropbox/FlashPOD/Machine 3/" + folder_month + "/" + folder_name + "/"
# )
# path_P4 = (
#     "E:/FlashPOD Dropbox/FlashPOD/Machine 4/" + folder_month + "/" + folder_name + "/"
# )

path_line = "E:/THANGVT/tools/arranger_v2.2/arrange-PDF-files/end_of_folder_line.pdf"
path_P1 = "E:/Dropbox/Machine 1/2023_11/" + folder_name + "/"
path_P2 = "E:/Dropbox/Machine 2/2023_11/" + folder_name + "/"
path_P3 = "E:/Dropbox/Machine 3/2023_11/" + folder_name + "/"
path_P4 = "E:/Dropbox/Machine 4/2023_11/" + folder_name + "/"

P1 = date + "_P1_"
P2 = date + "_P2_"
P3 = date + "_P3_"
P4 = date + "_P4_"

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

    def __str__(self):
        return f"{self.order_code}{self.side}{self.size}{self.color}{self.set}{self.seller}"

    def __del__(self):
        return


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
        path = os.path.join(path_P3, P3 + "SET")
    elif order.color == "BLACK":
        # if order.side == "FB":
        #     path = os.path.join(
        #         path_P4, P4 + order.color + "_" + order.size + "_" + order.side
        #     )
        # else:
        path = os.path.join(path_P4, P4 + order.color + "_" + order.size)
    elif order.color == "WHITE":
        # if order.side == "FB":
        #     path = os.path.join(
        #         path_P3,
        #         P3 + order.color + "_" + order.size + "_" + order.side,
        #     )
        # else:
        path = os.path.join(path_P3, P3 + order.color + "_" + order.size)
    else:
        path = os.path.join(
            path_P1,
            P1 + order.color,
        )
    return path


list_path = []


def core():
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

    for path1 in list_path:
        shutil.copy(
            path_line,
            path1,
        )


def main():
    core()
    os.system("pause")


main()
