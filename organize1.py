import os
import shutil
from pathlib import Path

os.chdir("D:/OrganizeFiles/Input")

for file in os.listdir():
    name, size = os.path.splitext(file)
    splitted = name.split("_")
    splitted = [s.strip() for s in splitted]
    if (splitted[5] == "1-1"):
        if (splitted[2] == "3XL-BLACK") or (splitted[2] == "3XL-WHITE"):
            if(splitted[1] == "FB"):
                shutil.move(file,"D:/OrganizeFiles/Output/3XL LARGE FB")
            else: 
                shutil.move(file,"D:/OrganizeFiles/Output/3XL LARGE")
        elif (splitted[2] == "2XL-BLACK") or (splitted[2] == "2XL-WHITE"):
            if(splitted[1] == "FB"):
                shutil.move(file,"D:/OrganizeFiles/Output/2XL LARGE FB")
            else: 
                shutil.move(file,"D:/OrganizeFiles/Output/2XL LARGE")            
        elif (splitted[2] == "L-BLACK") or (splitted[2] == "L-WHITE"):
            if(splitted[1] == "FB"):
                shutil.move(file,"D:/OrganizeFiles/Output/LARGE FB")
            else: 
                shutil.move(file,"D:/OrganizeFiles/Output/LARGE")
        elif (splitted[2] == "M-BLACK") or (splitted[2] == "M-WHITE"):
            if(splitted[1] == "FB"):
                shutil.move(file,"D:/OrganizeFiles/Output/MEDIUM FB")
            else:
                shutil.move(file,"D:/OrganizeFiles/Output/MEDIUM")
        elif (splitted[2] == "XL-BLACK") or (splitted[2] == "XL-WHITE"):
            if(splitted[1] == "FB"):
                shutil.move(file,"D:/OrganizeFiles/Output/XL LARGE FB")
            else:
                shutil.move(file,"D:/OrganizeFiles/Output/XL LARGE")
        else:
            shutil.move(file,"D:/OrganizeFiles/Output/SMALL")
    else :
        shutil.move(file,"D:/OrganizeFiles/Output/SET")