import requests
from bs4 import BeautifulSoup
import pandas as pd
import shutil
import urllib.request
import urllib
import os

LIST_PREFIX = [
    "https://drive.google.com/file/d/",
    "https://drive.google.com/uc?id=",
    "/view?usp=drive_link",
    "/view?usp=sharing",
]

list = pd.read_csv(r"E:\THANGVT\tools\arranger_v2.2\arrange-PDF-files\label_hod001.csv")

print(list)
# list_url = []

for i in range(0, len(list)):
    for j in LIST_PREFIX:
        link = str(list["linklabel"][i].replace(j, ""))
        list.at[i, "linklabel"] = link

print(list)

for i in range(0, len(list)):
    url = (
        "https://drive.google.com/u/0/uc?id="
        + str(list["linklabel"][i])
        + "&export=download"
    )
    r = requests.get(url)
    filename = os.path.join("", url.split("/")[-1])
    with open(
        "E:/THANGVT/tools/arranger_v2.2/arrange-PDF-files/download/filename", "wb"
    ) as f:
        f.write(r.content)
