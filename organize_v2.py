import os
import shutil
from pathlib import Path

pathInput = "F:/OrganizeFIles/Input"
pathOutput = "F:/OrganizeFIles/Output/"
pathNewOrder = pathOutput + "DON MOI/"
pathColor = pathNewOrder + "COLORS/"
pathOutputRoot = "F:/OrganizeFIles/Output"

sizeList = {
    "3XL LARGE",
    "2XL LARGE",
    "XL LARGE",
    "MEDIUM",
    "SET",
    "SMALL",
    "LARGE",
}

sizeListFB = {
    "3XL LARGE FB",
    "2XL LARGE FB",
    "XL LARGE FB",
    "MEDIUM FB",
    "SET FB",
    "LARGE FB",
}

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

typeList = ["MUGS", "DON UU TIEN", "IARTGROUP", "FIX ISSUES"]


def createTemplate():
    isExist = os.path.exists(pathOutputRoot)
    if isExist:
        shutil.rmtree(pathOutputRoot)
        print("Old files was deleted !!!")
    print("Now creating new files...")
    print("----------------------------------------------------------------")
    for typer in typeList:
        os.makedirs(pathOutput + typer)
        print(pathOutput + typer + " ... created")
    for size in sizeList:
        os.makedirs(pathNewOrder + size)
        print(pathNewOrder + size + " ... created")
    for sizefb in sizeListFB:
        os.makedirs(pathNewOrder + sizefb)
        print(pathNewOrder + sizefb + " ... created")
    os.makedirs(pathColor)
    for color in colorList:
        os.makedirs(pathColor + color)
        print(pathColor + color + " ... created")
    print("----------------------------------------------------------------")
    print("Templates created <3")


def organizeFilesByColor():
    os.chdir(pathInput)
    for file in os.listdir():
        name, size = os.path.splitext(file)
        splitByUnderline = name.split("_")
        splitted = [s.strip() for s in splitByUnderline]
        if splitted[3] == "size" or splitted[3] == "2" or splitted[3] == "1":
            shutil.move(file, pathNewOrder + "SMALL")
        else:
            splitByColor = splitted[2].split("-")
            for color in colorList:
                if splitByColor[1] == color:
                    shutil.move(file, pathColor + color)


def organizeFilesBySize():
    os.chdir(pathInput)
    print("Organizing files...")
    print("----------------------------------------------------------------")
    for file in os.listdir():
        name, size = os.path.splitext(file)
        splitByUnderline = name.split("_")
        splitted = [s.strip() for s in splitByUnderline]
        if splitted[5] == "1-1":
            splitBySize = splitted[2].split("-")
            match splitBySize[0]:
                case "3XL":
                    if splitted[1] == "FB":
                        shutil.move(file, pathNewOrder + "3XL LARGE FB")
                    else:
                        shutil.move(file, pathNewOrder + "3XL LARGE")
                case "2XL":
                    if splitted[1] == "FB":
                        shutil.move(file, pathNewOrder + "2XL LARGE FB")
                    else:
                        shutil.move(file, pathNewOrder + "2XL LARGE")
                case "XL":
                    if splitted[1] == "FB":
                        shutil.move(file, pathNewOrder + "XL LARGE FB")
                    else:
                        shutil.move(file, pathNewOrder + "XL LARGE")
                case "L":
                    if splitted[1] == "FB":
                        shutil.move(file, pathNewOrder + "LARGE FB")
                    else:
                        shutil.move(file, pathNewOrder + "LARGE")
                case "M":
                    if splitted[1] == "FB":
                        shutil.move(file, pathNewOrder + "MEDIUM FB")
                    else:
                        shutil.move(file, pathNewOrder + "MEDIUM")
        elif splitted[1] == "FB":
            shutil.move(file, pathNewOrder + "SET FB")
        else:
            shutil.move(file, pathNewOrder + "SET")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("----------------------------------------------------------------")
    print("DONE :v")


def main():
    key = input("Tao mới folder nhập 0, chia tiếp files nhập 1: ")
    if key == "0":
        createTemplate()
        organizeFilesByColor()
        organizeFilesBySize()
    elif key == "1":
        organizeFilesByColor()
        organizeFilesBySize()
    else:
        exit


main()
