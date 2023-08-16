import os
import shutil
from pathlib import Path
from tkinter import *
from tkinter import filedialog
import datetime
import mysql.connector

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
    ["3XL", "2XL", "XL", "L", "M"],
    ["3XL LARGE", "2XL LARGE", "XL LARGE", "LARGE", "MEDIUM", "SET"],
    ["3XL LARGE FB","2XL LARGE FB","XL LARGE FB","LARGE FB","MEDIUM FB","SET FB",]
]

dataFolder = [
    ["3XL LARGE", "2XL LARGE", "XL LARGE", "LARGE", "MEDIUM", "SET", "SMALL"],
    ["3XL LARGE FB","2XL LARGE FB","XL LARGE FB","LARGE FB","MEDIUM FB","SET FB",]
]

typeList = ["MUGS", "DON UU TIEN", "FIX ISSUES"]

STATUS = "UPLOADED"


def updateDB(status, orderCode):
    conn = mysql.connector.connect(
    host = "seller.flashship.net", 
    user = "flashship", 
    password = "sjvnZVc6cwqUzk", 
    database = "fplatform",
    auth_plugin='mysql_native_password'
    )
    connObj = conn.cursor()
    querySmall = "UPDATE orders SET status = %s where order_code = %s"
    val = (status, orderCode)
    connObj.execute(querySmall, val)
    conn.commit()
    conn.close()
    
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
    for size in dataFolder[0]:
        os.makedirs(pathNewOrder + size)  # create folder by sizeList
        print(pathNewOrder + size + " ... CREATED!")
    for sizefb in dataFolder[1]:
        os.makedirs(pathNewOrder + sizefb)  # create folder by sizeListFB
        print(pathNewOrder + sizefb + " ... CREATED!")
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
    inputQuantity = 0 # for counting files in input
    for file in os.listdir():
        name, size = os.path.splitext(file)
        splitByUnderline = name.split("_")  # get data that was splitted by "_"
        splitted = [s.strip() for s in splitByUnderline]
        orderCode = splitted[4]
        orderCodeS = splitted[3]
        splitByColor = splitted[2].split("-")  # get data that was splitted by "-"
        if splitByColor[0] == "S":
            shutil.move(file, pathNewOrder + "SMALL")
            countColor += 1
            updateDB(STATUS,orderCodeS)
        elif splitted[5] != "1-1":  # Arrange files by SET and SET FB
            if splitted[1] == "FB":
                shutil.move(file, pathNewOrder + "SET FB")
                countColor += 1
                updateDB(STATUS,orderCode)
            else:
                shutil.move(file, pathNewOrder + "SET")
                countColor += 1
                updateDB(STATUS,orderCode)
        else:
            for color in colorList:
                if splitByColor[1] == color:
                    shutil.move(file, pathColor + color)
                    countColor += 1
                    updateDB(STATUS,orderCode)
        inputQuantity += 1
    print(" ", inputQuantity, "FILES IN INPUT:")
    print(" ", countColor, "FILES BY COLOR DONE.")


# Arrange files by Sizes: 3XL, 2XL,... in data[]
def arrangeFilesBySize():
    os.chdir(pathInput)
    countSize = 0  # for counting files
    for file in os.listdir():
        name, size = os.path.splitext(file)
        splitByUnderline = name.split("_")  # get data that was splitted by "_"
        splitted = [
            s.strip() for s in splitByUnderline
        ]  # xóa khoảng trắng 2 đầu string
        orderCode = splitted[4]
        splitBySize = splitted[2].split("-")  # get data that was splitted by "-"
        for i in range(5):
            if splitBySize[0] == data[0][i]:
                if splitted[1] == "FB":
                    shutil.move(file, pathNewOrder + data[2][i])
                    countSize += 1
                    updateDB(STATUS,orderCode)
                else:
                    shutil.move(file, pathNewOrder + data[1][i])
                    countSize += 1
                    updateDB(STATUS,orderCode)
    print(" ", countSize, "FILES DONE")


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
    
main()
