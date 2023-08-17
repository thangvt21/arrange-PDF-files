import os
import shutil
from pathlib import Path
from tkinter import *
from tkinter import filedialog
import datetime
import mysql.connector

today = datetime.datetime.now()
folderName = str(today.month) + "_" + str(today.day)
pathInput = "E:/US/PDFFILES/Input/"
pathOutput = "E:/OneDrive - VAB/FS - POD/THANG 8/" + folderName + "/"
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
    ["3XL", "2XL", "XL", "L", "M"],
    ["3XL LARGE", "2XL LARGE", "XL LARGE", "LARGE", "MEDIUM", "SET"],
    [
        "3XL LARGE FB",
        "2XL LARGE FB",
        "XL LARGE FB",
        "LARGE FB",
        "MEDIUM FB",
        "SET FB",
    ],
]

dataFolder = [
    "3XL LARGE",
    "2XL LARGE",
    "XL LARGE",
    "LARGE",
    "MEDIUM",
    "SET",
    "SMALL",
    "3XL LARGE FB",
    "2XL LARGE FB",
    "XL LARGE FB",
    "LARGE FB",
    "MEDIUM FB",
    "SET FB",
]

typeList = ["MUGS", "DON UU TIEN", "FIX ISSUES"]

STATUS = "UPLOADED"


def splittedByUnderline(file):
    name, size = os.path.splitext(file)
    splitByUnderline = name.split("_")  # get data that was splitted by "_"
    splitted = [s.strip() for s in splitByUnderline]
    return splitted


def splittedByExtension(file):
    name, size = file.split(".pdf")
    splitByUnderline = name.split("_")
    splitted = [s.strip() for s in splitByUnderline]
    return splitted


def selectOrder():
    conn = mysql.connector.connect(
        host="seller.flashship.net",
        user="flashship",
        password="sjvnZVc6cwqUzk",
        database="fplatform",
        auth_plugin="mysql_native_password",
    )
    connObj = conn.cursor()
    query = "SELECT quantity,variant_id,both_side,front_size_image,back_size_image FROM order_produst WHERE FIND_IN_SET(order_produst) GROUP BY orrder_id, line_id"
    conn.close()


def updateDB(status, orderCode):
    conn = mysql.connector.connect(
        host="seller.flashship.net",
        user="flashship",
        password="sjvnZVc6cwqUzk",
        database="fplatform",
        auth_plugin="mysql_native_password",
    )
    connObj = conn.cursor()
    querySmall = "UPDATE orders SET status = %s where order_code = %s"
    val = (status, orderCode)
    connObj.execute(querySmall, val)
    conn.commit()
    conn.close()


# Choose file path of folder that contains Input và Output (need create folder Input before running tool; folder Output will be automatically created)
# def getNewPathInput(pathInput, pathOutput):
#     print("SELECT FOLDER THAT CONTAINS INPUT: ")
#     root = Tk()  # open tkinter dialog
#     filepathRoot = filedialog.askdirectory()  # get root path
#     pathInput = filepathRoot + "/Input/"
#     pathOutput = filepathRoot + "/Output/"
#     root.withdraw()  # Hide tkinter dialog
#     print("- - - - - - - - - - - - - - - - - - -")
#     print("  INPUT DIRECTORY: ", pathInput)
#     print("  OUTPUT DIRECTORY: ", pathOutput)
#     print("- - - - - - - - - - - - - - - - - - -")


# Create document directory by Sizes và Colors, folder Output will be automatically created
def createTemplate():
    print("- - - - - - - - - - - - - - - - - - -")
    print("NOW CREATING NEW FOLDERS.")
    for typer in typeList:  # create folder by typeList
        os.makedirs(pathOutput + typer)
        print(pathOutput + typer + " ... CREATED!")
    for size in dataFolder:
        os.makedirs(pathNewOrder + size)  # create folder by sizeList
        print(pathNewOrder + size + " ... CREATED!")
    os.makedirs(pathColor)  # create folder by colorList
    for color in colorList:
        os.makedirs(pathColor + color)
        print(pathColor + color + " ... CREATED!")
    print("TEMPLATES CREATED.")
    print("- - - - - - - - - - - - - - - - - - -")


# Arrange files by Colors: RED, NAVY, ROYALBLUE, ... in colorList[]
def arrangeFilesByColor():
    os.chdir(pathInput)
    countColor = 0  # for counting arranged files
    inputQuantity = 0  # for counting files in input
    for file in os.listdir():
        splitted = splittedByUnderline(file)
        splitByColor = splitted[2].split("-")  # get data that was splitted by "-"
        if splitByColor[0] == "S":
            shutil.move(file, pathNewOrder + "SMALL")
            countColor += 1
        elif splitted[5] != "1-1":  # Arrange files by SET and SET FB
            if splitted[1] == "FB":
                shutil.move(file, pathNewOrder + "SET FB")
                countColor += 1
            else:
                shutil.move(file, pathNewOrder + "SET")
                countColor += 1
        else:
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
    for file in os.listdir():
        splitted = splittedByUnderline(file)  # xóa khoảng trắng 2 đầu string
        splitBySize = splitted[2].split("-")  # get data that was splitted by "-"
        for i in range(5):
            if splitBySize[0] == data[0][i]:
                if splitted[1] == "FB":
                    shutil.move(file, pathNewOrder + data[2][i])
                    countSize += 1
                else:
                    shutil.move(file, pathNewOrder + data[1][i])
                    countSize += 1
    print(" ", countSize, "FILES DONE")


# Use os.walk() for browsing all directories
def browseFoldersAndUpdateDB():
    count = 0
    for root, dirs, files in os.walk(
        "E:/OneDrive - VAB/FS - POD/THANG 8/8.16/DON MOI/"
    ):
        for file in files:
            if file.endswith(".pdf"):
                splitted = splittedByExtension(file)
                print(splitted)


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

    browseFoldersAndUpdateDB()


main()
