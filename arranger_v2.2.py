import os
import shutil
from pathlib import Path
from tkinter import *
from tkinter import filedialog

pathInput = "E:/US/PDFFILES/Input/"
pathOutput = "E:/US/PDFFILES/Output/"
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
]

data = [
    ["3XL", "2XL", "XL", "L", "M", "S"],
    ["3XL LARGE", "2XL LARGE", "XL LARGE", "LARGE", "MEDIUM", "SMALL", "SET"],
    [
        "3XL LARGE FB",
        "2XL LARGE FB",
        "XL LARGE FB",
        "LARGE FB",
        "MEDIUM FB",
        "SMALL FB",
        "SET FB",
    ],
]

typeList = ["MUGS", "DON UU TIEN", "IARTGROUP", "FIX ISSUES"]


# Chọn đường dẫn đến thư mục sẽ chứa thư mục Input và Output (cần tạo trước folder Input; folder Output sẽ tự động tạo khi chạy app)
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


# Tạo cây thư mục theo Sizes và Colors, folder Output sẽ tự động tạo ra bên trong đường dẫn được chọn
def createTemplate():
    print("OLD FOLDERS WILL BE REMOVED!")
    print("- - - - - - - - - - - - - - - - - - -")
    isExist = os.path.exists(pathOutput)
    if isExist:
        shutil.rmtree(pathOutput)
    print("OLD FOLDERS WERE REMOVED!")
    print("- - - - - - - - - - - - - - - - - - -")
    print("NOW CREATING NEW FOLDERS.")
    for typer in typeList:  # tạo folder theo typeList
        os.makedirs(pathOutput + typer)
        print(pathOutput + typer + " ... CREATED!")
    for size in data[1]:
        os.makedirs(pathNewOrder + size)  # tạo folder theo sizeList
        print(pathNewOrder + size + " ... CREATED!")
    for sizefb in data[2]:
        os.makedirs(pathNewOrder + sizefb)  # tạo folder theo sizeListFB
        print(pathNewOrder + sizefb + " ... CREATED!")
    os.makedirs(pathColor)  # tạo folder theo colorList
    for color in colorList:
        os.makedirs(pathColor + color)
        print(pathColor + color + " ... CREATED!")
    print("TEMPLATES CREATED.")
    print("- - - - - - - - - - - - - - - - - - -")


# Chia files vào các folder theo các màu: RED, NAVY, ROYALBLUE, ... có trong colorList[]
def arrangeFilesByColor():
    os.chdir(pathInput)
    count = 0  # for counting files
    for file in os.listdir():
        name, size = os.path.splitext(file)
        splitByUnderline = name.split("_")  # lấy data phân cách theo dấu "_"
        splitted = [s.strip() for s in splitByUnderline]
        splitByColor = splitted[2].split("-")  # lấy data phân cách theo dấu "-"
        for color in colorList:
            if splitByColor[1] == color:
                shutil.move(file, pathColor + color)
                count += 1
    print(" ", count, "FILES BY COLOR DONE.")


# Chia files vào các folder theo các sizes: 3XL, 2XL,... có trong data[]
def arrangeFilesBySize():
    os.chdir(pathInput)
    count = 0  # for counting files
    for file in os.listdir():
        name, size = os.path.splitext(file)
        splitByUnderline = name.split("_")  # lấy data phân cách theo dấu "_"
        splitted = [
            s.strip() for s in splitByUnderline
        ]  # xóa khoảng trắng 2 đầu string
        splitBySize = splitted[2].split("-")  # lấy data phân cách theo dấu "-"
        if splitted[5] != "1-1":  # Sắp xếp files SET và SET FB
            if splitted[1] == "FB":
                shutil.move(file, pathNewOrder + "SET FB")
                count += 1
            else:
                shutil.move(file, pathNewOrder + "SET")
                count += 1
        else:
            for i in range(6):
                if splitBySize[0] == data[0][i]:
                    if splitted[1] == "FB":
                        shutil.move(file, pathNewOrder + data[2][i])
                        count += 1
                    else:
                        shutil.move(file, pathNewOrder + data[1][i])
                        count += 1

    print(" ", count, "FILES BY SIZE DONE.")


def main():
    # key1 = input(
    #     " NHẬP 0 - ĐỂ CHỌN FOLDER CHỨA INPUT VÀ OUTPUT (NHẤN BẤT KỲ ĐỂ THOÁT): "
    # )
    # if key1 == "0":
    #     getNewPathInput(pathInput, pathOutput)
    print("0. ĐỂ XÓA FOLDER CŨ VÀ TẠO FOLDERS MỚI")
    print("1. ĐỂ CHIA TIẾP FILES VÀO FOLDERS CŨ")
    key2 = input("NHẬP SỐ: ")
    if key2 == "0":
        createTemplate()
        print("VICTOR'S TOOL IS WORKING...")
        print("- - - - - - - - - - - - - - - - - - -")
        arrangeFilesByColor()
        arrangeFilesBySize()
        os.system("pause")
    elif key2 == "1":
        print("VICTOR'S TOOL IS WORKING...")
        print("- - - - - - - - - - - - - - - - - - -")
        arrangeFilesByColor()
        arrangeFilesBySize()
        os.system("pause")
    else:
        exit


# else:
#     exit


main()
