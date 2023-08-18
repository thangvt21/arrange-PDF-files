import os
import shutil
import datetime
import pandas as pd
import sqlalchemy as db


today = datetime.datetime.now()
FOLDER_NAME = str(today.month) + "_" + str(today.day)
PATH_INPUT = "E:/US/PDFFILES/Input/"
PATH_OUTPUT = "E:/OneDrive - VAB/FS - POD/THANG 8/" + FOLDER_NAME + "/"
PATH_NEW_ORDER = PATH_OUTPUT + "DON MOI/"
PATH_COLOR = PATH_NEW_ORDER + "COLORS/"


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
    "SET",
    "SMALL",
    "3XL LARGE FB",
    "2XL LARGE FB",
    "XL LARGE FB",
    "LARGE FB",
    "MEDIUM FB",
    "SET FB",
]


TYPE_LIST = ["MUGS", "DON UU TIEN", "FIX ISSUES"]

STATUS = "UPLOADED"


def create_template():
    """create folder template for uploading"""
    print("- - - - - - - - - - - - - - - - - - -")
    print("NOW CREATING NEW FOLDERS.")
    for typer in TYPE_LIST:  # create folder by typeList
        os.makedirs(PATH_OUTPUT + typer)
        print(PATH_OUTPUT + typer + " ... CREATED!")
    for size in DATA_FOLDER:
        os.makedirs(PATH_NEW_ORDER + size)  # create folder by sizeList
        print(PATH_NEW_ORDER + size + " ... CREATED!")
    os.makedirs(PATH_COLOR)  # create folder by colorList
    for color in COLOR_LIST:
        os.makedirs(PATH_COLOR + color)
        print(PATH_COLOR + color + " ... CREATED!")
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


# Arrange files by Colors: RED, NAVY, ROYALBLUE, ... in colorList[]
def arrange_files_by_color():
    """arrange files by colors"""
    os.chdir(PATH_INPUT)
    count_color = 0  # for counting arranged files
    input_quantity = 0  # for counting files in input
    for file in os.listdir():
        splitted = splitted_by_underline(file)  # get data that was splitted by "-"
        # print(splitted)  # print
        if splitted[2] == "S":
            shutil.move(file, PATH_NEW_ORDER + "SMALL")
            count_color += 1
        elif splitted[7] != "1":  # Arrange files by SET and SET FB
            if splitted[1] == "FB":
                shutil.move(file, PATH_NEW_ORDER + "SET FB")
                _count_color += 1
            else:
                shutil.move(file, PATH_NEW_ORDER + "SET")
                count_color += 1
        else:
            for color in COLOR_LIST:
                if splitted[3] == color:
                    shutil.move(file, PATH_COLOR + color)
                    _count_color += 1
        input_quantity += 1
    print(" ", input_quantity, "FILES IN INPUT:")
    print(" ", count_color, "FILES BY COLOR DONE.")


def arrange_files_by_size():
    """# Arrange files by Sizes: 3XL, 2XL,... in data[]"""
    os.chdir(PATH_INPUT)
    count_size = 0  # for counting files
    for file in os.listdir():
        splitted = splitted_by_underline(
            file
        )  # xóa khoảng trắng 2 đầu string  # get data that was splitted by "-"
        for i in range(5):
            if splitted[2] == DATA[0][i]:
                if splitted[1] == "FB":
                    shutil.move(file, PATH_NEW_ORDER + DATA[2][i])
                    count_size += 1
                else:
                    shutil.move(file, PATH_NEW_ORDER + DATA[1][i])
                    count_size += 1
    print(" ", count_size, "FILES DONE")


def get_data_by_size_from_table_order_product(df_input):
    """Get data by size from order_product

    Args:
        df (pandas.dataframe): dataframe

    Returns:
        pandas.dataframe: data by size
    """
    connection_string = (
        "mysql+pymysql://flashship:sjvnZVc6cwqUzk@seller.flashship.net:3306/fplatform"
    )
    engine = db.create_engine(connection_string)
    connection = engine.connect()
    query = "SELECT order_product.order_id, orders.order_code, order_product.line_id, order_product.product_name, order_product.quantity, order_product.both_side FROM order_product JOIN orders WHERE order_product.order_id = orders.id AND orders.order_code IN %(values)s AND order_product.created > '2023-08-15' AND order_product.created < '2023-08-17' GROUP BY order_product.order_id, order_product.line_id"
    vari = {
        "values": df_input["order_code"].astype(str).tolist(),
    }
    df_res = pd.read_sql(query, connection, params=vari)
    engine.dispose()
    return df_res


# Use os.walk() for browsing all directories
def browse_folders_for_pdf_files(path):
    """browse for finding .pdf files in a given directory (path)

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
    for _, _, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                splitted = splitted_by_extension(file)
                if len(splitted) > 9:
                    splitted = splitted[:-1]
                df_pdf.loc[len(df_pdf)] = splitted
    df_mlxl = df_pdf[df_pdf["size"] != "S"]
    df_s = df_pdf[df_pdf["size"] == "S"]
    data_mlxl = get_data_by_size_from_table_order_product(df_mlxl)
    data_s = get_data_by_size_from_table_order_product(df_s)
    print(data_mlxl)
    print(data_s)


def update_order_status(order_code, status):
    """Update order status to table orders

    Args:
        order_code (String): order code
        status (String): status of order
    """
    connection_string = (
        "mysql+pymysql://flashship:sjvnZVc6cwqUzk@seller.flashship.net:3306/fplatform"
    )
    engine = db.create_engine(connection_string)
    conn = engine.connect()
    meta = db.MetaData()
    orders = db.Table("orders", meta, autoload_with=engine)
    stmt = (
        db.update(orders).where(orders.c.order_code == order_code).values(status=status)
    )
    conn.execute(stmt)
    conn.commit()
    engine.dispose()


def main():
    """Main function"""
    # print("0. TẠO FOLDERS MỚI")
    # print("1. ĐỂ CHIA TIẾP FILES VÀO FOLDERS CŨ")
    # key2 = input("NHẬP SỐ: ")
    # if key2 == "0":
    #     create_template()
    #     print("VICTOR'S TOOL IS WORKING...")
    #     print("- - - - - - - - - - - - - - - - - - -")
    #     arrange_files_by_color()
    #     arrange_files_by_size()
    #     os.system("pause")
    # elif key2 == "1":
    #     print("VICTOR'S TOOL IS WORKING...")
    #     print("- - - - - - - - - - - - - - - - - - -")
    #     arrange_files_by_color()
    #     arrange_files_by_size()
    #     os.system("pause")
    # else:
    #     exit
    # path2Browse = "E:/OneDrive - VAB/FS - POD/THANG 8/8.16/DON MOI/"
    # browse_folders_for_pdf_files(path2Browse)

    status = "UPLOADED"
    order_code = "8OEM9DIIN"
    update_order_status(order_code, status)


main()
