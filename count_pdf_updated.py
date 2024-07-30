import os
import datetime

today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_root = str(today.year) + "_" + str(today.month)
# folder_name = "2024_6_4"
# folder_root = "2024_6"


def get_path(machine):
    path_root = (
        "D:/FlashPOD Dropbox/FlashPOD/Machine "
        + str(machine)
        + "/"
        + folder_root
        + "/"
        + folder_name
        + "/"
    )
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
    while key != "0":
        key = input("Nhập 1 để đếm PDF (Nhập 0 để dừng): ")
        if key == "1":
            sum = 0
            print("DATE: ", folder_name)
            for m in MACHINE_LIST:
                count = 0
                path = get_path(m)
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.endswith(".pdf"):
                            count += 1
                sum += count
                if m < 10:
                    print("Machine 0" + str(m), ":", count)
                else:
                    print("Machine " + str(m), ":", count)
            print("Tổng:", sum)


main()
