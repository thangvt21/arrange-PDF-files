import os
import shutil
import datetime

today = datetime.datetime.now()
folder_name = str(today.month) + "." + str(today.day)
folder_name_P2 = str(today.month) + "." + str(today.day - 1) + " P2"
folder_root = "THANG" + str(today.month)

path1 = "D:/FlashPOD Dropbox/FlashPOD/Machine 1/2023_11/2023_11_10"
path2 = "D:/FlashPOD Dropbox/FlashPOD/Machine 2/2023_11/2023_11_10"
path3 = "D:/FlashPOD Dropbox/FlashPOD/Machine 3/2023_11/2023_11_10"
path4 = "D:/FlashPOD Dropbox/FlashPOD/Machine 4/2023_11/2023_11_10"

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
print(count1)
print(count2)
print(count3)
print(count4)
print(count1 + count2 + count3 + count4)
