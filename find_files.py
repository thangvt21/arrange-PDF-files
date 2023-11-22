import os
import shutil
import datetime

today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_root = str(today.year) + "_" + str(today.month)

path1 = "E:/FlashPOD Dropbox/FlashPOD/Machine 1/2023_11/2023_11_19/"
path2 = "E:/FlashPOD Dropbox/FlashPOD/Machine 2/2023_11/2023_11_19/"
path3 = "E:/FlashPOD Dropbox/FlashPOD/Machine 3/2023_11/2023_11_19/"
path4 = "E:/FlashPOD Dropbox/FlashPOD/Machine 4/2023_11/2023_11_19/"


path5 = "E:/FlashPOD Dropbox/Thang Vo/1_Đạt_TSHIRT_only/15_11_2023/TEMP/DONE"

path_tshirt = "E:/FlashPOD Dropbox/Thang Vo/20231111_P2/20231111_Tshirt/"
path_hoodie = "E:/FlashPOD Dropbox/Thang Vo/20231111_P2/20231111_Hoodie/"
path_sweatshirt = "E:/FlashPOD Dropbox/Thang Vo/20231111_P2/20231111_Sweatshirt/"

PATH_LIST = [path1, path2, path3, path4, path5]
count = 0
for i, path in enumerate(PATH_LIST, start=1):
    for root, dirs, files in os.walk(path):
        for file in files:
            if "end_of_folder_line.pdf" == file:
                count += 1

print(count)
