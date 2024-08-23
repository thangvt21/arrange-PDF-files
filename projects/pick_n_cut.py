import os
import datetime
import pygsheets
import pandas as pd

today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_root = str(today.year) + "_" + str(today.month)

DROPBOX_PATH = "D:\\FlashPOD Dropbox\\FlashPOD\\"

JSON_PATH = (
    "E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\luminous-lodge-321503-2defcccdcd2d.json"
)

SHEET_ID = "1zPjUEOQ8iyHGvL_rfjJWRpAo63hTVKjEx_tCUFFax4k"

MACHINE_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]


def count_order(path):
    for _, _, _ in os.walk(path):
        count_pdf = 0
        name = os.path.basename(path)
        if name[-2] == "_":
            res = name[:-2]
        else:
            res = name[:-3]
        return res, count_pdf


def main():
    i = 1
    gc = pygsheets.authorize(service_account_file=JSON_PATH)
    spreadsheet = gc.open_by_key(SHEET_ID)
    worksheet = spreadsheet.worksheet_by_title("PICK/CUT")
    worksheet.clear(start="A2", end="Z300")
    for m in MACHINE_LIST:
        machine_path = os.path.join(
            DROPBOX_PATH, "Machine " + str(m) + "\\" + folder_root + "\\" + folder_name
        )
        lst_folder = []
        for _, dirs, _ in os.walk(machine_path):
            for d in dirs:
                patho = os.path.join(machine_path, d)
                res = count_order(patho)
                lst_folder.append(res[0])
        df = pd.DataFrame(lst_folder)
        worksheet.set_dataframe(df, start=(2, i), copy_head=False)
        i += 1


main()
