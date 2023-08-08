import os
import shutil
from pathlib import Path
from tkinter import *
from tkinter import filedialog
import datetime

today = datetime.datetime.now()
folderName = str(today.month) + "." + str(today.day)
pathInput = "E:/US/PDFFILES/Input/"
pathOutput = "E:/OneDrive - VAB/FS - POD/THANG 8/" + folderName +"/"
pathNewOrder = pathOutput + "DON MOI/"
pathColor = pathNewOrder + "COLORS/"


colorList = [
    "RED",
    "NAVY",
    "ROYALBLUE",
    "LIGHTBLUE",
    "CHARCOAL",
    "DARKHEATHER",
    "SPORTGREY",
    "MAROON",
    "SAND",
    "LIGHTPINK", 
]

data = [
    ["3XL", "2XL", "XL", "L", "M", "S"],
    ["3XL LARGE", "2XL LARGE", "XL LARGE", "LARGE", "MEDIUM", "SET", "SMALL"],
    ["3XL LARGE FB","2XL LARGE FB","XL LARGE FB","LARGE FB","MEDIUM FB","SET FB",]
]

typeList = ["MUGS", "DON UU TIEN", "FIX ISSUES"]


# Choose file path of folder that contains Input và Output (need create folder Input before running tool; folder Output will be automatically created)
def getNewPathInput(pathInput, pathOutput):
    print("SELECT FOLDER THAT CONTAINS INPUT: ")
    root = Tk()  # open tkinter dialog
    filepathRoot = filedialog.askdirectory()  # get root path
    pathInput = filepathRoot + "/Input/"
    pathOutput = filepathRoot + "/Output/"
    root.withdraw()  # Hide tkinter dialog
    print("- - - - - - - - - - - - - - - - - - -")
    print("  INPUT DIRECTORY: ", pathInput)
    print("  OUTPUT DIRECTORY: ", pathOutput)
    print("- - - - - - - - - - - - - - - - - - -")


# Create document directory by Sizes và Colors, folder Output will be automatically created
def createTemplate():
    print("- - - - - - - - - - - - - - - - - - -")
    print("NOW CREATING NEW FOLDERS.")
    for typer in typeList:  # create folder by typeList
        os.makedirs(pathOutput + typer)
        print(pathOutput + typer + " ... CREATED!")
    for size in data[1]:
        os.makedirs(pathNewOrder + size)  # create folder by sizeList
        print(pathNewOrder + size + " ... CREATED!")
    for sizefb in data[2]:
        os.makedirs(pathNewOrder + sizefb)  # create folder by sizeListFB
        print(pathNewOrder + sizefb + " ... CREATED!")
    os.makedirs(pathColor)  # create folder by colorList
    for color in colorList:
        os.makedirs(pathColor + color)
        print(pathColor + color + " ... CREATED!")
    print("TEMPLATES CREATED.")
    print("- - - - - - - - - - - - - - - - - - -")


# Count shirts
def countShirt():
    os.chdir(pathInput)
    countSize = 0  # for counting files
    countFB = 0 # for counting files FB
    shirts = 0 # for counting shirts
    shirtsFB = 0 # for counting shirts have FB
    for file in os.listdir():
        name, size = os.path.splitext(file)
        splitByUnderline = name.split("_")  # get data that was splitted by "_"
        splitted = [
            s.strip() for s in splitByUnderline
        ]  # xóa khoảng trắng 2 đầu string
        splitBySize = splitted[2].split("-")  # get data that was splitted by "-"
        if splitted[5] != "1-1":  # Arrange files by SET and SET FB
            if splitted[1] == "FB":
                countFB += 1
            else:
                countSize += 1
        else:
            for i in range(6):
                if splitBySize[0] == data[0][i]:
                    if splitted[1] == "FB":
                        countFB += 1
                    else:
                        countSize += 1
    shirtsFB = countFB / 2
    shirts = countSize
    print(" ", shirtsFB, "SHIRTS-FB DONE.")
    print(" ", shirts, "SHIRTS DONE.")


# Arrange files by Colors: RED, NAVY, ROYALBLUE, ... in colorList[]
def arrangeFilesByColor():
    os.chdir(pathInput)
    countColor = 0  # for counting arranged files
    inputQuantity = 0 # for counting files in input
    for file in os.listdir():
        name, size = os.path.splitext(file)
        splitByUnderline = name.split("_")  # get data that was splitted by "_"
        splitted = [s.strip() for s in splitByUnderline]
        splitByColor = splitted[2].split("-")  # get data that was splitted by "-"
        for color in colorList:
            if splitByColor[1] == color:
                shutil.move(file, pathColor + color)
                countColor += 1
        inputQuantity += 1
    print(" ", inputQuantity, "FILES IN INPUT:")
    print(" ", countColor, "FILES BY COLOR DONE.")


# Arrange files by Sizes: 3XL, 2XL,... in data[]
def arrangeFilesBySize():
    os.chdir(pathInput)
    countSize = 0  # for counting files
    countFB = 0 # for counting files FB
    shirts = 0 # for counting shirts
    shirtsFB = 0 # for counting shirts have FB
    for file in os.listdir():
        name, size = os.path.splitext(file)
        splitByUnderline = name.split("_")  # get data that was splitted by "_"
        splitted = [
            s.strip() for s in splitByUnderline
        ]  # xóa khoảng trắng 2 đầu string
        splitBySize = splitted[2].split("-")  # get data that was splitted by "-"
        if splitted[5] != "1-1":  # Arrange files by SET and SET FB
            if splitted[1] == "FB":
                shutil.move(file, pathNewOrder + "SET FB")
                countFB += 1
            else:
                shutil.move(file, pathNewOrder + "SET")
                countSize += 1
        else:
            for i in range(6):
                if splitBySize[0] == data[0][i]:
                    if splitted[1] == "FB":
                        shutil.move(file, pathNewOrder + data[2][i])
                        countFB += 1
                    else:
                        shutil.move(file, pathNewOrder + data[1][i])
                        countSize += 1
    print(" ", countFB+countSize, "FILES DONE")

# def countSmall():
#     pathSmall = pathNewOrder + "/SMALL"
#     os.chdir(pathSmall)
#     for file in os.listdir():
#         name, size = os.path.splitext(file)
#         splitByUnderline = name.split("_")  # get data that was splitted by "_"
#         splitted = [
#             s.strip() for s in splitByUnderline
#         ] 
#         print(len(splitByUnderline))

def main():
    # key1 = input(
    #     " NHẬP 0 - ĐỂ CHỌN FOLDER CHỨA INPUT VÀ OUTPUT (NHẤN BẤT KỲ ĐỂ THOÁT): "
    # )
    # if key1 == "0":
    #     getNewPathInput(pathInput, pathOutput)
    print("0. TẠO FOLDERS MỚI")
    print("1. ĐỂ CHIA TIẾP FILES VÀO FOLDERS CŨ")
    key2 = input("NHẬP SỐ: ")
    if key2 == "0":
        createTemplate()
        print("VICTOR'S TOOL IS WORKING...")
        print("- - - - - - - - - - - - - - - - - - -")
        countShirt()
        arrangeFilesByColor()
        arrangeFilesBySize()
        # countSmall()
        os.system("pause")
    elif key2 == "1":
        print("VICTOR'S TOOL IS WORKING...")
        print("- - - - - - - - - - - - - - - - - - -")
        countShirt()
        arrangeFilesByColor()
        arrangeFilesBySize()
        # countSmall()
        os.system("pause")
    else:
        exit

main()
