import os
import shutil
import datetime

today = datetime.datetime.now()
folder_name = str(today.month) + "." + str(today.day)
folder_name_P2 = str(today.month) + "." + str(today.day - 1) + " P2"
folder_root = "THANG" + str(today.month)

path = "E:/FlashPOD Dropbox/FlashPOD/THANG 11/" + folder_name + "/"
path2 = "E:/FlashPOD Dropbox/FlashPOD/THANG 11/" + folder_name_P2 + "/"
count = 0
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".pdf"):
            count += 1
print(count)
