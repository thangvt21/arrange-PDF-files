import os
import datetime

today = datetime.datetime.now()
# folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
# folder_root = str(today.year) + "_" + str(today.month)
folder_name = "2024_5_20"
folder_root = "2024_5"

path1 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 1/" + folder_root + "/" + folder_name + "/"
)
path2 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 2/" + folder_root + "/" + folder_name + "/"
)
path3 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 3/" + folder_root + "/" + folder_name + "/"
)
path4 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 4/" + folder_root + "/" + folder_name + "/"
)
path5 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 5/" + folder_root + "/" + folder_name + "/"
)
path6 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 6/" + folder_root + "/" + folder_name + "/"
)
path7 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 7/" + folder_root + "/" + folder_name + "/"
)
path8 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 8/" + folder_root + "/" + folder_name + "/"
)
path9 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 9/" + folder_root + "/" + folder_name + "/"
)
path10 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 10/" + folder_root + "/" + folder_name + "/"
)

path20 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 20/" + folder_root + "/" + folder_name + "/"
)

path21 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 21/" + folder_root + "/" + folder_name + "/"
)

path22 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 22/" + folder_root + "/" + folder_name + "/"
)

path23 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 23/" + folder_root + "/" + folder_name + "/"
)

path24 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 24/" + folder_root + "/" + folder_name + "/"
)

path25 = (
    "D:/FlashPOD Dropbox/FlashPOD/Machine 25/" + folder_root + "/" + folder_name + "/"
)

PATH_LIST = [
    path1,
    path2,
    path3,
    path4,
    path5,
    path6,
    path7,
    path8,
    path9,
    path10,
    path20,
    path21,
    path22,
    path23,
    path24,
    path25,
]


def main():
    key = ""
    while key != "0":
        key = input("Nhập 1 để đếm PDF (Nhập 0 để dừng): ")
        if key == "1":
            sum = 0
            for path in PATH_LIST:
                count = 0
                path_str1 = path.split("/")
                path_str2 = [s.strip() for s in path_str1]
                machine = str(path_str2[3])
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.endswith(".pdf"):
                            count += 1
                sum += count
                print(machine, ":", count)
                # print(path)
            print("Tổng:", sum)


main()
