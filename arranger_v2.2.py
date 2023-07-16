import os
import shutil
from pathlib import Path

pathInput = "D:/work/Chiafile/Input/"
pathOutput = "D:/work/Chiafile/Output/"
pathNewOrder = pathOutput + "DON MOI/"
pathColor = pathNewOrder + "COLORS/"
pathOutputRoot = "D:/work/Chiafile/Output"

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
    ["3XL","2XL","XL","L","M","S"],
    ["3XL LARGE","2XL LARGE","XL LARGE","LARGE","MEDIUM","SMALL","SET"],
    ["3XL LARGE FB","2XL LARGE FB","XL LARGE FB","LARGE FB","MEDIUM FB","SMALL FB","SET FB"],
]

typeList = ["MUGS", "DON UU TIEN", "IARTGROUP", "FIX ISSUES"]


def createTemplate():
    isExist = os.path.exists(pathOutputRoot)
    if isExist:
        shutil.rmtree(pathOutputRoot)
        print("Old files was deleted !!!")
    print("Now creating new folders...")
    for typer in typeList:
        os.makedirs(pathOutput + typer)
        print(pathOutput + typer + " ... created")
    for size in data[1]:
        os.makedirs(pathNewOrder + size)
        print(pathNewOrder + size + " ... created")
    for sizefb in data[2]:
        os.makedirs(pathNewOrder + sizefb)
        print(pathNewOrder + sizefb + " ... created")
    os.makedirs(pathColor)
    for color in colorList:
        os.makedirs(pathColor + color)
        print(pathColor + color + " ... created")
    print("Templates created.")


def arrangeFilesByColor():
    os.chdir(pathInput)
    count = 0
    for file in os.listdir():
        name, size = os.path.splitext(file)
        splitByUnderline = name.split("_")
        splitted = [s.strip() for s in splitByUnderline]
        splitByColor = splitted[2].split("-")
        for color in colorList:
            if splitByColor[1] == color:
                    shutil.move(file, pathColor + color)
        count += 1
    print(count, "FILES BY COLOR DONE.")


def arrangeFilesBySize():
    os.chdir(pathInput)
    count = 0
    for file in os.listdir():
        name, size = os.path.splitext(file)
        splitByUnderline = name.split("_")
        splitted = [s.strip() for s in splitByUnderline]
        splitBySize = splitted[2].split("-")
        if splitted[5] != "1-1":
            if splitted[1] == "FB":
                shutil.move(file, pathNewOrder + "SET FB")
            else:
                shutil.move(file, pathNewOrder + "SET")
        else:
            for i in range(6):
                if splitBySize[0] == data[0][i]:
                    if splitted[1] == "FB":
                        shutil.move(file, pathNewOrder + data[2][i])
                    else:
                        shutil.move(file, pathNewOrder + data[1][i])
        count += 1
    print(count, "FILES BY SIZE DONE.")

def main():
    key = input("Tao mới folder nhập 0, chia tiếp files nhập 1: ")
    if key == "0":
        createTemplate()
        print("Organizing files...")
        arrangeFilesByColor()
        arrangeFilesBySize()
    elif key == "1":
        print("Organizing files...")
        arrangeFilesByColor()
        arrangeFilesBySize()
    else:
        exit

main()