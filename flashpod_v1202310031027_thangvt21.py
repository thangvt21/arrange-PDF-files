"""Modules
    Author: thangvt21
    Github: https://github.com/thangvt21
"""
import os
import shutil
import datetime
import pandas as pd
import sqlalchemy as db


today = datetime.datetime.now()
FOLDER_NAME = str(today.month) + "." + str(today.day)
FOLDER_NAME_P2 = str(today.month) + "." + str(today.day - 1)


# PATHS ONEDRIVE
PATH_INPUT = "E:/US/PDFFILES/Input"
PATH_OUTPUT = "E:/FlashPOD Dropbox/FlashPOD/THANG 10/" + FOLDER_NAME + "/"
PATH_NEW_ORDER = PATH_OUTPUT + "DON MOI/"
PATH_COLOR = PATH_NEW_ORDER + "COLORS/"
PATH_BLACK = PATH_NEW_ORDER + "BLACK/"
PATH_WHITE = PATH_NEW_ORDER + "WHITE/"


# PATHS DROPBOX
PATH_INPUT_DROPBOX = "E:/US/PDFFILES/Input"
# PATH_OUTPUT_DROPBOX = "E:/Dropbox/THANG 10/" + FOLDER_NAME + "/"
PATH_OUTPUT_DROPBOX = "E:/FlashPOD Dropbox/FlashPOD/THANG 10/" + FOLDER_NAME + "/"
PATH_OUTPUT_DROPBOX_P2 = (
    "E:/FlashPOD Dropbox/FlashPOD/THANG 10/" + FOLDER_NAME_P2 + "/" + FOLDER_NAME + "/"
)
PATH_NEW_ORDER_DROPBOX = PATH_OUTPUT_DROPBOX + "DON MOI/"
PATH_COLOR_DROPBOX = PATH_NEW_ORDER_DROPBOX + "COLORS/"
PATH_BLACK_DROPBOX = PATH_NEW_ORDER_DROPBOX + "BLACK/"
PATH_WHITE_DROPBOX = PATH_NEW_ORDER_DROPBOX + "WHITE/"


# LISTS
LIST_FOLDER_S_SET = ["SMALL", "SET", "SET FB"]

OTHERS_LIST = [
    "MERCHFOXSUPPORT",
    "MBTEAM",
    "SUPPORTTUAN",
    "PHAMPHONGPHU",
    "NGUYENTHUY",
    "TDATEAMSUPPORT",
]

COLOR_LIST = [
    "RED",
    "NAVY",
    "ROYALBLUE",
    "LIGHTBLUE",
    "CHARCOAL",
    "DARKHEATHER",
    "SPORTGREY",
    "MAROON",
    "SAND",
    "LIGHTPINK",
    "FORESTGREEN",
]

DATA = [
    ["3XL", "2XL", "XL", "L", "M"],
    ["3XL LARGE", "2XL LARGE", "XL LARGE", "LARGE", "MEDIUM", "SET"],
    [
        "3XL LARGE FB",
        "2XL LARGE FB",
        "XL LARGE FB",
        "LARGE FB",
        "MEDIUM FB",
        "SET FB",
    ],
]

DATA_FOLDER = [
    "3XL LARGE",
    "2XL LARGE",
    "XL LARGE",
    "LARGE",
    "MEDIUM",
    "3XL LARGE FB",
    "2XL LARGE FB",
    "XL LARGE FB",
    "LARGE FB",
    "MEDIUM FB",
]

CORE_COLORS = ["BLACK", "WHITE"]

TYPE_LIST = ["DON UU TIEN", "FIX ISSUES", "KHACH TU MUA LABEL", "HOODIES"]

# STATUS = "UPLOADED"


def create_template():
    """create folder template for uploading"""
    print("- - - - - - - - - - - - - - - - - - -")
    print("NOW CREATING NEW FOLDERS.")
    for typer in TYPE_LIST:  # create folder by typeList
        # os.makedirs(PATH_OUTPUT + typer)
        os.makedirs(PATH_OUTPUT_DROPBOX + typer)
        # print(PATH_OUTPUT + typer + " ... CREATED!")
        print(PATH_OUTPUT_DROPBOX + typer + " ... CREATED!")
    # for size in DATA_FOLDER:
    #     os.makedirs(PATH_NEW_ORDER + size)  # create folder by sizeList
    #     print(PATH_NEW_ORDER + size + " ... CREATED!")
    for core in CORE_COLORS:  # create folder by sizeList
        # os.makedirs(PATH_NEW_ORDER + core)
        os.makedirs(PATH_NEW_ORDER_DROPBOX + core)
    for size in DATA_FOLDER:
        # os.makedirs(PATH_BLACK + size)
        os.makedirs(PATH_BLACK_DROPBOX + size)
        # os.makedirs(PATH_WHITE + size)  # create folder by sizeList
        os.makedirs(PATH_WHITE_DROPBOX + size)
        # print(PATH_BLACK + size + " ... CREATED!")
        print(PATH_BLACK_DROPBOX + size + " ... CREATED!")
        # print(PATH_WHITE + size + " ... CREATED!")
        print(PATH_WHITE_DROPBOX + size + " ... CREATED!")
    # os.makedirs(PATH_NEW_ORDER + "SMALL")
    # os.makedirs(PATH_NEW_ORDER + "SET")
    # os.makedirs(PATH_NEW_ORDER + "SET FB")
    # os.makedirs(PATH_COLOR)
    os.makedirs(PATH_NEW_ORDER_DROPBOX + "SMALL")
    os.makedirs(PATH_NEW_ORDER_DROPBOX + "SET")
    os.makedirs(PATH_NEW_ORDER_DROPBOX + "SET FB")
    os.makedirs(PATH_COLOR_DROPBOX)
    # create folder by colorList
    for color in COLOR_LIST:
        # os.makedirs(PATH_COLOR + color)
        os.makedirs(PATH_COLOR_DROPBOX + color)
        # print(PATH_COLOR + color + " ... CREATED!")
        print(PATH_COLOR_DROPBOX + color + " ... CREATED!")
    print("TEMPLATES CREATED.")
    print("- - - - - - - - - - - - - - - - - - -")


def splitted_by_underline(file):
    """get word that splited by underline

    Args:
        file (_.pdf_): file with .pdf extension

    Returns:
        list: list of words
    """
    name, _ = os.path.splitext(file)
    name = name.replace("-", "_")
    split_by_underline = name.split("_")  # get data that was splitted by "_"
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


def find_file(root_directory, target_file):
    for root, dirs, files in os.walk(root_directory):
        if target_file in files:
            return os.path.join(root, target_file)
    return None


def organize_by_seller():
    os.chdir(PATH_INPUT_DROPBOX)
    count_seller = 0
    for file in os.listdir():
        splitted = splitted_by_underline(file)
        for other in OTHERS_LIST:
            if len(splitted) == 17:
                if splitted[8] == other or splitted[16] == other:
                    shutil.move(file, PATH_OUTPUT_DROPBOX + "KHACH TU MUA LABEL")
            elif len(splitted) != 17 and splitted[8] == other:
                shutil.move(file, PATH_OUTPUT_DROPBOX + "KHACH TU MUA LABEL")


# Organize_files_by_color files by Colors: RED, NAVY, ROYALBLUE, ... in colorList[]
def organize_by_color():
    os.chdir(PATH_INPUT_DROPBOX)
    for file in os.listdir():
        for color in COLOR_LIST:
            splitted = splitted_by_underline(file)
            if splitted[4] == color:
                if splitted[6] != "1":  # Arrange files by SET and SET FB
                    if splitted[2] == "FB":
                        shutil.move(file, PATH_NEW_ORDER_DROPBOX + "SET FB")
                    else:
                        shutil.move(file, PATH_NEW_ORDER_DROPBOX + "SET")
                else:
                    shutil.move(file, PATH_COLOR_DROPBOX + color)


def organize_by_small():
    """organize files by colors"""
    os.chdir(PATH_INPUT_DROPBOX)
    for file in os.listdir():
        splitted = splitted_by_underline(file)  # get data that was splitted by "-"
        if splitted[3] == "S":
            if len(splitted) == 9:
                if splitted[6] != "1":
                    shutil.move(file, PATH_NEW_ORDER_DROPBOX + "SET")
                else:
                    shutil.move(file, PATH_NEW_ORDER_DROPBOX + "SMALL")
            elif len(splitted) == 17:
                if splitted[6] != "1" or splitted[14] != "1":
                    shutil.move(file, PATH_NEW_ORDER_DROPBOX + "SET")
                else:
                    shutil.move(file, PATH_NEW_ORDER_DROPBOX + "SMALL")
        elif splitted[6] != "1":  # Arrange files by SET and SET FB
            if splitted[2] == "FB":
                shutil.move(file, PATH_NEW_ORDER_DROPBOX + "SET FB")
            else:
                shutil.move(file, PATH_NEW_ORDER_DROPBOX + "SET")
        # else:
        #     for color in COLOR_LIST:
        #         if splitted[4] == color:
        #             shutil.move(file, PATH_COLOR_DROPBOX + color)


def organize_by_size():
    """# organize files by sizes"""
    os.chdir(PATH_INPUT_DROPBOX)
    count_size = 0  # for counting files
    for file in os.listdir():
        file2 = file
        splitted = splitted_by_underline(file)
        if splitted[4] == "BLACK":
            for i in range(5):
                if splitted[3] == DATA[0][i]:
                    if splitted[2] == "FB":
                        # shutil.move(file, PATH_BLACK + DATA[2][i])
                        shutil.move(file, PATH_BLACK_DROPBOX + DATA[2][i])
                    else:
                        # shutil.move(file, PATH_BLACK + DATA[1][i])
                        shutil.move(file, PATH_BLACK_DROPBOX + DATA[1][i])
        elif splitted[4] == "WHITE":
            for i in range(5):
                if splitted[3] == DATA[0][i]:
                    if splitted[2] == "FB":
                        # shutil.move(file, PATH_WHITE + DATA[2][i])
                        shutil.move(file, PATH_WHITE_DROPBOX + DATA[2][i])
                    else:
                        # shutil.move(file, PATH_WHITE + DATA[1][i])
                        shutil.move(file, PATH_WHITE_DROPBOX + DATA[1][i])

    def getdata_bysize_from_db_order_product(df_input):
        """Get data by size from order_product

        Args:
            df (pandas.dataframe): dataframe

        Returns:
            pandas.dataframe: data by size
        """
        param_values = {
            "values": df_input["order_code"].astype(str).tolist(),
            "date_from": "2023-08-15",
            "date_to": "2023-08-18",
        }
        connection_string = "mysql+pymysql://flashship:sjvnZVc6cwqUzk@seller.flashship.net:3306/fplatform"
        engine = db.create_engine(connection_string)
        conn = engine.connect()
        meta = db.MetaData()
        product_check = db.Table("product_check", meta, autoload_with=engine)
        stmt = db.select(
            product_check.c[
                "order_id",
                "order_code",
                "line_id",
                "product_name",
                "quantity",
                "front_image_size",
                "back_image_size",
                "both_side",
            ]
        ).where(
            (product_check.c.order_code.in_(db.bindparam("values", expanding=True)))
            & (product_check.c.created > db.bindparam("date_from"))
            & (product_check.c.created < db.bindparam("date_to"))
        )
        result = conn.execute(
            stmt,
            param_values,
        )
        res = result.fetchall()
        engine.dispose()
        df_res = pd.DataFrame(
            {
                "order_id": [],
                "order_code": [],
                "line_id": [],
                "product_name": [],
                "quantity": [],
                "front_image_size": [],
                "back_image_size": [],
                "both_side": [],
            }
        )
        for item in res:
            df_res.loc[len(df_res)] = item
        return df_res

    def browse_folders_for_pdf_files(path):
        """browse for finding .pdf files in a given directory (path)
        using os.walk() for browsing all directories
        Args:
            path (String): path of the directory
        """
        df_pdf = pd.DataFrame(
            {
                "seller": [],
                "both_side": [],
                "size": [],
                "color": [],
                "group_id": [],
                "order_code": [],
                "quantity": [],
                "total": [],
                "side": [],
            }
        )
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".pdf"):
                    splitted = splitted_by_extension(file)
                    if len(splitted) > 9:
                        splitted = splitted[:-1]
                    df_pdf.loc[len(df_pdf)] = splitted
        df_mlxl = df_pdf[df_pdf["size"] != "S"]
        df_s = df_pdf[df_pdf["size"] == "S"]
        data_mlxl = getdata_bysize_from_db_order_product(df_mlxl)
        data_s = getdata_bysize_from_db_order_product(df_s)
        mlxl_count = data_mlxl["order_code"].value_counts()
        s_count = data_s["order_code"].value_counts()
        print(mlxl_count, s_count)

    def update_order_status(order_code, status):
        """Update order status to table orders

         Args:
        order_code (String): order code
        status (String): status of order
        """
        connection_string = "mysql+pymysql://flashship:sjvnZVc6cwqUzk@seller.flashship.net:3306/fplatform"
        engine = db.create_engine(connection_string)
        conn = engine.connect()
        meta = db.MetaData()
        orders = db.Table("orders", meta, autoload_with=engine)
        stmt = (
            db.update(orders)
            .where(orders.c.order_code == order_code)
            .values(status=status)
        )
        conn.execute(stmt)
        conn.commit()
        engine.dispose()


def count_files():
    sum_files = 0
    sum_files_dropbox = 0
    print("  " + "WHITE :")
    for folder in DATA_FOLDER:
        # _, _, file_white = next(os.walk(PATH_WHITE + folder))
        _, _, file_white_dropbox = next(os.walk(PATH_WHITE_DROPBOX + folder))
        # sum_files += len(file_white)
        sum_files_dropbox += len(file_white_dropbox)
        # if len(file_white) > 0:
        #     print("   ", folder, len(file_white))
        if len(file_white_dropbox) > 0:
            print("   ", folder, len(file_white_dropbox), "DROPBOX")
    print("---------------------------------------------------")
    print("  " + "BLACK :")
    for folder1 in DATA_FOLDER:
        # _, _, file_black = next(os.walk(PATH_BLACK + folder1))
        _, _, file_black_dropbox = next(os.walk(PATH_BLACK_DROPBOX + folder1))
        # sum_files += len(file_black)
        sum_files_dropbox += len(file_black_dropbox)
        # if len(file_black) > 0:
        #     print("   ", folder1, len(file_black))
        if len(file_black_dropbox) > 0:
            print("   ", folder1, len(file_black_dropbox), "DROPBOX")
    print("---------------------------------------------------")
    print("  " + "COLORS :")
    for folder_color in COLOR_LIST:
        # _, _, file_color = next(os.walk(PATH_COLOR + folder_color))
        _, _, file_color_dropbox = next(os.walk(PATH_COLOR_DROPBOX + folder_color))
        # sum_files += len(file_color)
        sum_files_dropbox += len(file_color_dropbox)
        # if len(file_color) > 0:
        #     print("   ", folder_color, len(file_color))
        if len(file_color_dropbox) > 0:
            print("   ", folder_color, len(file_color_dropbox), "DROPBOX")
    print("---------------------------------------------------")
    for folder0 in LIST_FOLDER_S_SET:
        # _, _, file0 = next(os.walk(PATH_NEW_ORDER + folder0))
        _, _, file0_dropbox = next(os.walk(PATH_NEW_ORDER_DROPBOX + folder0))
        # sum_files += len(file0)
        sum_files_dropbox += len(file0_dropbox)
        # if len(file0) > 0:
        # print("   ", folder0, len(file0))
        if len(file0_dropbox) > 0:
            print("   ", folder0, len(file0_dropbox), "DROPBOX")
    print("---------------------------------------------------")
    # print("DON MOI: ", sum_files)
    print("DON MOI DROPBOX: ", sum_files_dropbox)
    for folder2 in TYPE_LIST:
        # _, _, files = next(os.walk(PATH_OUTPUT + folder2))
        _, _, files_dropbox = next(os.walk(PATH_OUTPUT_DROPBOX + folder2))
        # if len(files) > 0:
        #     print(folder2 + " : ", len(files))
        if len(files_dropbox) > 0:
            print(folder2 + " : ", len(files_dropbox), "DROPBOX")
    print("---------------------------------------------------")
    print("DONE.")


def core():
    """Core function"""
    print("0. TẠO FOLDERS MỚI")
    print("1. ĐỂ CHIA TIẾP FILES VÀO FOLDERS CŨ")
    key2 = input("NHẬP SỐ: ")
    if key2 == "0":
        create_template()
        print("- - - - - - - - - - - - - - - - - - -")
        print("VICTOR'S TOOL IS WORKING...")
        print("- - - - - - - - - - - - - - - - - - -")
        organize_by_seller()
        organize_by_color()
        organize_by_small()
        organize_by_size()
        count_files()
        os.system("pause")
    elif key2 == "1":
        print("- - - - - - - - - - - - - - - - - - -")
        print("VICTOR'S TOOL IS WORKING...")
        print("- - - - - - - - - - - - - - - - - - -")
        organize_by_seller()
        organize_by_color()
        organize_by_small()
        organize_by_size()
        print("VICTOR IS COUNTING FILES... ")
        print("---------------------------------------------------")
        count_files()
        os.system("pause")


def main():
    """Main function"""
    core()

    # path_2_browse = "E:/OneDrive - VAB/FS - POD/THANG 8/8.16/DON MOI/"
    # browse_folders_for_pdf_files(path_2_browse)

    # status = "UPLOADED"
    # order_code = "8OEM9DIIN"
    # update_order_status(order_code, status)


main()
