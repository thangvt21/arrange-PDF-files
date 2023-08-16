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

def countSmall():
    shirts = 0
    pathSmall = pathNewOrder + "/SMALL"
    os.chdir(pathSmall)
    for file in os.listdir():
        name, size = os.path.splitext(file)
        splitByUnderline = name.split("_")  # get data that was splitted by "_"
        splitted = [
            s.strip() for s in splitByUnderline
        ] 
        if len(splitByUnderline) == 6 :
            shirts += 1
        else:
            if splitted[4] == splitted[5]:
                shirts += 1
            else:
                shirts += 2
    print("tổng số áo size S: ",shirts)
    

def main():
    countSmall()
    
main()    