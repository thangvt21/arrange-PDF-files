import os
import datetime

today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_root = str(today.year) + "_" + str(today.month)
# folder_name = "2024_1_15"
# folder_root = "2024_1"

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
path_tshirt = "D:/FlashPOD Dropbox/Thang Vo/20231111_P2/20231111_Tshirt/"
path_hoodie = "D:/FlashPOD Dropbox/Thang Vo/20231111_P2/20231111_Hoodie/"
path_sweatshirt = "D:/FlashPOD Dropbox/Thang Vo/20231111_P2/20231111_Sweatshirt/"

PATH_LIST = [path1, path2, path3, path4, path5, path6, path7, path8]


def main():
    key = ""
    while key != "0":
        key = input("Nhập 1 để đếm PDF (Nhập 0 để dừng): ")
        if key == "1":
            sum = 0
            for i, path in enumerate(PATH_LIST, start=1):
                count = 0
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.endswith(".pdf"):
                            count += 1
                sum += count
                print(f"Machine {i}:", count)
            print(sum)


main()
