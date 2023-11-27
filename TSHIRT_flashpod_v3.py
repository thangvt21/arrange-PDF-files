import os
import shutil
import datetime
import arrow

today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_month = str(today.year) + "_" + str(today.month)
date = str(arrow.now().format("YYYYMMDD"))

path_input = "D:/work/Chiafile/Input"
# path_output = "D:/Dropbox/THANG 11/" + folder_name + "/"
path_output = "D:/Dropbox/2023_11/"
# path_output = "D:/FlashPOD Dropbox/Thang Vo/THANG 11/" + folder_name + "/"

# date = str(today.year) + str(today.month) + str(today.day)


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
            phân tách bởi dấu "-" hoặc "_"
            Để tách keyword cho tùy mục đích sử dụng (chia file, thống kê)
    Args:
        File

    Actions:
        Thay thế dấu "-" thành dấu "_" để đồng nhất
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
    # match splitted[3]:
    #     case "S":
    #         splitted[3] = "SMALL"
    #     case "M":
    #         splitted[3] = "MEDIUM"
    #     case "L":
    #         splitted[3] = "LARGE"
    #     case "XL":
    #         splitted[3] = "XL LARGE"
    #     case "2XL":
    #         splitted[3] = "2XL LARGE"
    #     case default:
    #         splitted[3] = "3XL LARGE"
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
    for seller in SELF_LABEL:
        if order.seller == seller:
            path = os.path.join(
                path_output,
                "P3",
                date + "_P3_" + order.color + "_" + order.size + "_TSHIRT_" + "SL",
            )
            return path
        elif order.set != "1":
            path = os.path.join(path_output, "P3", date + "_P3_SET")
        elif order.color == "BLACK":
            if order.side == "FB":
                path = os.path.join(
                    path_output,
                    "P4",
                    # "1-NORMAL",
                    date + "_P4_" + order.color + "_" + order.size + "_" + order.side,
                )
            else:
                path = os.path.join(
                    path_output,
                    "P4",
                    # "1-NORMAL",
                    date + "_P4_" + order.color + "_" + order.size,
                )
        elif order.color == "WHITE":
            if order.side == "FB":
                path = os.path.join(
                    path_output,
                    "P2",
                    # "1-NORMAL",
                    date + "_P2_" + order.color + "_" + order.size + "_" + order.side,
                )
            else:
                path = os.path.join(
                    path_output,
                    "P2",
                    # "1-NORMAL",
                    date + "_P2_" + order.color + "_" + order.size,
                )
        else:
            path = os.path.join(path_output, "P2", date + "_P2_" + order.color)
    return path


def count_pdf(path):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                count += 1
    return count


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
            "D:/work/TSHIRT/tool/arrange-PDF-files/end_of_folder_line.pdf",
            path1,
        )


def main():
    core()


main()
