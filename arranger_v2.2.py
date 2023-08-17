import os
import shutil
from pathlib import Path
from tkinter import *
from tkinter import filedialog
import datetime
import mysql.connector
import pandas as pd

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


def splittedByUnderline(file):
    name, size = os.path.splitext(file)
    name = name.replace("-", "_")
    splitByUnderline = name.split("_")  # get data that was splitted by "_"
    splitted = [s.strip() for s in splitByUnderline]
    return splitted


def splittedByExtension(file):
    name, size = file.split(".pdf")
    name = name.replace("-", "_")
    splitByUnderline = name.split("_")
    splitted = [s.strip() for s in splitByUnderline]
    return splitted


# Arrange files by Colors: RED, NAVY, ROYALBLUE, ... in colorList[]
def arrangeFilesByColor():
    os.chdir(pathInput)
    countColor = 0  # for counting arranged files
    inputQuantity = 0  # for counting files in input
    for file in os.listdir():
        splitted = splittedByUnderline(file)  # get data that was splitted by "-"
        # print(splitted)  # print
        if splitted[2] == "S":
            shutil.move(file, pathNewOrder + "SMALL")
            countColor += 1
        elif splitted[7] != "1":  # Arrange files by SET and SET FB
            if splitted[1] == "FB":
                shutil.move(file, pathNewOrder + "SET FB")
                countColor += 1
            else:
                shutil.move(file, pathNewOrder + "SET")
                countColor += 1
        else:
            for color in colorList:
                if splitted[3] == color:
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
        splitted = splittedByUnderline(
            file
        )  # xóa khoảng trắng 2 đầu string  # get data that was splitted by "-"
        for i in range(5):
            if splitted[2] == data[0][i]:
                if splitted[1] == "FB":
                    shutil.move(file, pathNewOrder + data[2][i])
                    countSize += 1
                else:
                    shutil.move(file, pathNewOrder + data[1][i])
                    countSize += 1
    print(" ", countSize, "FILES DONE")


# Use os.walk() for browsing all directories
def browseFolders(path):
    count = 0
    df = pd.DataFrame(
        {
            "seller": [],
            "both_side": [],
            "size": [],
            "color": [],
            "group_id": [],
            "order_code": [],
            "quantity": [],
            "total": [],
            "side": [],
        }
    )
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                splitted = splittedByExtension(file)
                if len(splitted) > 9:
                    splitted = splitted[:-1]
                df.loc[len(df)] = splitted
                # print(splitted)
    print(df)


def updateDB(status, orderCode):
    connection = mysql.connector.connect(
        host="seller.flashship.net",
        user="flashship",
        password="sjvnZVc6cwqUzk",
        database="fplatform",
        auth_plugin="mysql_native_password",
    )
    cursor = connection.cursor()
    querySmall = "UPDATE orders SET status = %s where order_code = %s"
    val = (status, orderCode)
    cursor.execute(querySmall, val)
    connection.commit()
    print(cursor.rowcount)
    connection.close()


def main():
    print("")
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
    # path2Browse = "E:/OneDrive - VAB/FS - POD/THANG 8/8.16/DON MOI/"
    # browseFolders(path2Browse)

    # status = "UPLOADED"
    # orderCode = "8OEM9DIIN"
    # updateDB(status, orderCode)
    # arrangeFilesByColor()


main()
