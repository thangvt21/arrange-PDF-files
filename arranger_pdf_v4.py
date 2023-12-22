import os
import shutil
import datetime
import arrow
import promptlib


today = datetime.datetime.now()
date = str(arrow.now().format("YYYYMMDD"))

folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_month = str(today.year) + "_" + str(today.month)

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
# path_P5 = (
#     "E:/FlashPOD Dropbox/FlashPOD/Machine 5/" + folder_month + "/" + folder_name + "/"
# )
# path_P6 = (
#     "E:/FlashPOD Dropbox/FlashPOD/Machine 6/" + folder_month + "/" + folder_name + "/"
# )

path_P1 = "E:/Dropbox/Machine 1/" + folder_month + "/" + folder_name + "/"
path_P2 = "E:/Dropbox/Machine 2/" + folder_month + "/" + folder_name + "/"
path_P3 = "E:/Dropbox/Machine 3/" + folder_month + "/" + folder_name + "/"
path_P4 = "E:/Dropbox/Machine 4/" + folder_month + "/" + folder_name + "/"
path_P5 = "E:/Dropbox/Machine 5/" + folder_month + "/" + folder_name + "/"
path_P6 = "E:/Dropbox/Machine 6/" + folder_month + "/" + folder_name + "/"

LIST_PATH = [path_P1, path_P2, path_P3, path_P4, path_P5, path_P6]

P1 = "TMP_" + date + "_P1_"
P2 = "TMP_" + date + "_P2_"
P3 = "TMP_" + date + "_P3_"
P4 = "TMP_" + date + "_P4_"
P5 = "TMP_" + date + "_P5_"
P6 = "TMP_" + date + "_P6_"

LIST_FOLDER = [P1, P2, P3, P4, P5, P6]

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


def count_pdf(path):
    for i, path in enumerate(path, start=1):
        count = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".pdf"):
                    count += 1
    return count


# def create_path(Order):
#     order = Order
#     if order.set != "1":
#         path = os.path.join(path_P6, P6 + "SET")
#     else:

#     return path


# def core():
#     os.chdir(path_input)
#     for file in os.listdir():
#         order = create_order(file)
#         path = create_path(order)
#         try:
#             if os.path.exists(path):
#                 shutil.move(file, path)
#             else:
#                 os.makedirs(path)
#                 shutil.move(file, path)
#         except IndexError as err:
#             print("Error: ", err)


def distribute_files(source_dir):
    files = [
        f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))
    ]
    num_files = len(files)
    num_dirs = round(num_files / 50)
    print(num_dirs)
    target_dirs = []
    print(os.path.join(LIST_PATH[1] + "_SHIRT_"))
    for j in range(0, num_dirs):
        num_path = len(LIST_PATH)
        dir_path = os.path.join(
            LIST_PATH[j % num_path],
            LIST_FOLDER[j % num_path] + "SHIRT_" + str(j + 1),
        )

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            target_dirs.append(dir_path)
        target_dirs.append(dir_path)
    print(target_dirs)
    num_dirss = len(target_dirs)
    for i, file in enumerate(files):
        target_dir = target_dirs[i % num_dirss]
        src_file = os.path.join(source_dir, file)
        dst_file = os.path.join(target_dir, file)
        shutil.copy(src_file, dst_file)


def main():
    distribute_files(path_input)


main()
