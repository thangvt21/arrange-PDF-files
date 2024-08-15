import os
import datetime
import pyinputplus as pyip
import logging


today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_root = str(today.year) + "_" + str(today.month)
log_file = today.strftime("%Y%m%d_%H%M%S")
# folder_name = "2024_6_4"
# folder_root = "2024_6"

logging.basicConfig(
    filename=f"E:\\THANGVT\\vtt_tools\\arrange-PDF-files\\logging\\{log_file}.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_path(machine):
    logging.debug("Get path: (%s)" % machine)
    path_root = (
        "D:/FlashPOD Dropbox/FlashPOD/Machine "
        + str(machine)
        + "/"
        + folder_root
        + "/"
        + folder_name
        + "/"
    )
    logging.debug("Path: (%s)" % path_root)
    return path_root


MACHINE_LIST = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
]


def main():
    key = ""
    while key != 0:
        key = pyip.inputInt("Nhập 1 để đếm PDF (Nhập 0 để dừng): ", min=0)
        if key == 1:
            total = 0
            print("DATE\t   :", folder_name)
            for m in MACHINE_LIST:
                logging.debug("Start get data from machine: (%s)" % m)
                count = 0
                path = get_path(m)
                for _, _, files in os.walk(path):
                    for file in files:
                        # logging.debug("File: (%s)" % (file))
                        if file.endswith(".pdf"):
                            count += 1
                total += count
                if m < 10:
                    print("Machine 0" + str(m), ":", count)
                else:
                    print("Machine " + str(m), ":", count)
            print("Tổng\t   :", total)
            # logging.debug("Machine (%s) has (%s)" % (m, count))


main()
