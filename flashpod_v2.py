import os
import shutil
import datetime

today = datetime.datetime.now()
folder_name = str(today.month) + "." + str(today.day)
folder_name_P2 = str(today.month) + "." + str(today.day - 1) + " P2"
folder_root = "THANG" + str(today.month)

path_input = "E:/US/PDFFILES/Input"
path_output = "E:/Dropbox/THANG 11/" + folder_name + "/"

""" 
    SELLER_LIST = ["DON MOI", "MERCHFOX"]
    COLOR = ["BLACK", "WHITE", "COLORS"]
    SIZE = ["SMALL", "MEDIUM", "LARGE", "XL LARGE", "2XL LARGE", "3XL LARGE"]
    POSITION = "FB"
    TYPE = ["SHIRT", "HOODIE", "SWEATSHIRT"]
    FOLDER_EXTRA = ["DON GUI LAI", "DON UU TIEN", "FIX ISSUES"]
""" 


def splitted_by_underline(file):
    """Thay thế dấu "-" thành dấu "_" để đồng nhất
    Tên file là String chứa các keyword :
    Tách các keyword phân cách bởi "_" thêm vào 1 list
    """
    name, _ = os.path.splitext(file)
    name = name.replace("-", "_")
    split_by_underline = name.split("_")
    splitted = [s.strip() for s in split_by_underline]
    return splitted


def splitted_by_extension(file):
    """get word that splited by .pdf extension

    Args:
        file (_.pdf_): file with .pdf extension

    Returns:
        list: list of words
    """
    name, _ = file.split(".pdf")
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
    match splitted[3]:
        case "S":
            splitted[3] = "SMALL"
        case "M":
            splitted[3] = "MEDIUM"
        case "L":
            splitted[3] = "LARGE"
        case "XL":
            splitted[3] = "XL LARGE"
        case "2XL":
            splitted[3] = "2XL LARGE"
        case default:
            splitted[3] = "3XL LARGE"
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
    if order.seller == "MERCHFOX":
        if order.set != "1":
            path = os.path.join(path_output, order.seller, "SET " + order.side)
        elif order.side == "FB":
            path = os.path.join(
                path_output, order.seller, order.color, order.size + " " + order.side
            )
        else:
            path = os.path.join(path_output, order.seller, order.color, order.size)
    else:
        if order.set != "1":
            path = os.path.join(path_output, "DON MOI", "SET " + order.side)
        elif order.side == "FB":
            path = os.path.join(
                path_output, "DON MOI", order.color, order.size + " " + order.side
            )
        else:
            path = os.path.join(path_output, "DON MOI", order.color, order.size)
    return path


def main():
    os.chdir(path_input)
    for file in os.listdir():
        order = create_order(file)
        path = create_path(order)
        try:
            if os.path.exists(path):
                shutil.move(file, path)
                # print(path_output)
                print("Completed")
            else:
                os.makedirs(path)
                shutil.move(file, path)
                print("Completed")
        except IndexError as err:
            print("Error: ", err)


main()