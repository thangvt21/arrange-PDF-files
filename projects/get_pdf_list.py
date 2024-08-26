import pandas as pd
import os
import pygsheets

folder_name = "2024_08_21"
folder_root = "2024_8"

json_dir = "E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\luminous-lodge-321503-2defcccdcd2d.json"
sheet_id = "1iZShXMaHGE_zyHwVkSSfa83dfMpb-qpHHLVXpS7ZxxI"
root = "F:\\Dropbox\\FlashPOD2\\"

machine_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

def split_by_underline(file):
    name, _ = os.path.splitext(file)
    name = name.replace("-", "_")
    transform_str = name.split("_")
    split = [s.strip() for s in transform_str]
    return split

class Order:
    def __init__(
        self,
        date,
        order_code,
        side1,
        size,
        color,
        set_number,
        set_order,
        side2,
        seller,
        product_type,
        provider,
    ):
        self.date = date
        self.order_code = order_code
        self.side1 = side1
        self.size = size
        self.color = color
        self.set_number = set_number
        self.set = set_order
        self.side2 = side2
        self.seller = seller
        self.product_type = product_type
        self.provider = provider

def create_order(file):
    split = split_by_underline(file)
    order = Order(
        split[0],
        split[3],
        split[4],
        split[2],
        split[1],
        split[5],
        split[6],
        split[7],
        split[8],
        split[9],
        split[10],
    )
    return order

def create_order_set(file):
    split = split_by_underline(file)
    order = Order(
        split[0],
        split[1],
        split[4],
        split[2],
        split[3],
        split[5],
        split[6],
        split[7],
        split[8],
        split[9],
        split[10],
    )
    return order

def count_shirts(order):
    variant = (
        order.order_code
        + " - "
        + order.seller
        # + "/"
        # + order.product_type
        # + "/"
        # + order.color
        # + "/"
        # + order.size
        # + " - "
        # + order.set_number
        # + "/"
        # + order.set
        # + " - "
        # + order.side
    )
    return variant

def get_pdf_list(path):
    for _, _, files in os.walk(path):
        list_var_raw = []
        # name = os.path.basename(path)
        for file in files:
            if file.endswith(".pdf"):
                split = split_by_underline(file)
                if split[6] != "1":
                    order = create_order_set(file)
                else:
                    order = create_order(file)
                variant = count_shirts(order)
                list_var_raw.append(variant)
        df = pd.DataFrame([sub.split(" - ") for sub in list_var_raw]).drop_duplicates()
        # df["count"] = df[1].map(df[1].value_counts())
        df.columns = ["order_code", "seller"]
        df.head()
        return df[["order_code", "seller"]].drop_duplicates()

def main():
    #Connect to Google Sheet
    global root
    gc = pygsheets.authorize(service_account_file=json_dir)
    spreadsheet = gc.open_by_key(sheet_id)
    worksheet = spreadsheet.worksheet_by_title("Machine 1")

    # Xóa ô ngày cũ
    worksheet.clear(start="A1", end="A1")

    # Xóa thống kê áo ngày cũ
    worksheet.clear(start="A3", end="D666")

    # Thêm ô ngày mới
    worksheet.update_value("A1", folder_name)

    pdf_list = []
    for m in machine_list:
        path_r = os.path.join(root, "Machine " + str(m) + "\\" + folder_root + "\\" + folder_name)
        for _, dirs, _ in os.walk(path_r):
            for d in dirs:
                patho = os.path.join(path_r, d)
                pdf_list.append(get_pdf_list(patho))

    sheet_row = 0
    for pdf in pdf_list:
        worksheet.set_dataframe(pdf, start=(3 + sheet_row, 1),copy_head=False)
        sheet_row = sheet_row + len(pdf)


main()
