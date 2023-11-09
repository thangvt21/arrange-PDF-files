import os
import shutil
import datetime
import arrow

today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_month = str(today.year) + "_" + str(today.month)
date = str(arrow.now().format("YYYYMMDD"))

path_input = "E:/US/PDFFILES/Input_SWEATSHIRT"

# path_P1 = "E:/FlashPOD Dropbox/FlashPOD/Machine 1/" + folder_name + "/"
# path_P2 = "E:/FlashPOD Dropbox/FlashPOD/Machine 2/" + folder_name + "/"
# path_P3 = "E:/FlashPOD Dropbox/FlashPOD/Machine 3/" + folder_name + "/"
# path_P4 = "E:/FlashPOD Dropbox/FlashPOD/Machine 4/" + folder_name + "/"

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
    """Tên file là dạng String gồm những keyword thể hiện các giá trị : date, seller, size, ... của product
            phân tách bởi dấu "_" hoặc "_"
            Để tách keyword cho tùy mục đích sử dụng (chia file, thống kê)
    Args:
        File

    Actions:
        Thay thế dấu "_" thành dấu "_" để đồng nhất
        Tách các keyword phân cách bởi "_"
        Xóa khoảng trắng đầu cuối
        Thêm keyword vào list splitted

    Return:
        List splitted chứa các keyword
    """
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
        splitted[1],
        splitted[2],
        splitted[3],
        splitted[4],
        splitted[5],
        splitted[6],
        splitted[8],
    )
    return order


def create_path(Order):
    order = Order
    order = Order
    if order.color == "BLACK":
        path = os.path.join(
            path_P3,
            P3 + "_" + order.color + "_SWSHIRT",
        )
    elif order.color == "WHITE":
        path = os.path.join(
            path_P3,
            P3 + order.color + "_SWSHIRT",
        )
    else:
        path = os.path.join(
            path_P3,
            P3 + order.color + "_SWSHIRT",
        )
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

    for path1 in list_path:
        shutil.copy(
            "E:/THANGVT/tools/arranger_v2.2/arrange-PDF-files/end_of_folder_line.pdf",
            path1,
        )


def main():
    core()


main()
