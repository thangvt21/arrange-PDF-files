import os
import shutil
import datetime

today = datetime.datetime.now()
folder_name = str(today.month) + "." + str(today.day)
folder_name_P2 = str(today.month) + "." + str(today.day - 1) + " P2"
folder_root = "THANG" + str(today.month)

path1 = "E:/FlashPOD Dropbox/FlashPOD/THANG 11/2023_11_8/20231108_P1/"
path2 = "E:/FlashPOD Dropbox/FlashPOD/THANG 11/2023_11_8/20231108_P2/"
path3 = "E:/FlashPOD Dropbox/FlashPOD/THANG 11/2023_11_8/20231108_P3/"
path4 = "E:/FlashPOD Dropbox/FlashPOD/THANG 11/2023_11_8/20231108_P4/"
count1 = 0
count2 = 0
count3 = 0
count4 = 0

for root, dirs, files in os.walk(path1):
    for file in files:
        if file.endswith(".pdf"):
            count1 += 1
for root, dirs, files in os.walk(path2):
    for file in files:
        if file.endswith(".pdf"):
            count2 += 1
for root, dirs, files in os.walk(path3):
    for file in files:
        if file.endswith(".pdf"):
            count3 += 1
for root, dirs, files in os.walk(path4):
    for file in files:
        if file.endswith(".pdf"):
            count4 += 1
print("P1: ", count1)
print("P2: ", count2)
print("P3: ", count3)
print("P4: ", count4)
print(count1 + count2 + count3 + count4)
