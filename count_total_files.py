import os
import datetime
import promptlib

today = datetime.datetime.now()
folder_name = str(today.year) + "_" + str(today.month) + "_" + str(today.day)
folder_root = str(today.year) + "_" + str(today.month)

prompter = promptlib.Files()
path_input = prompter.dir()


def main():
    count = 0
    for root, dirs, files in os.walk(path_input):
        for file in files:
            if file.endswith(".pdf"):
                count += 1
    print(count)


main()
