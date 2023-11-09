import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib
import os


LIST_PREFIX = [
    "https://drive.google.com/file/d/",
    "https://drive.google.com/uc?id=",
    "/view?usp=drive_link",
    "/view?usp=sharing",
]

list = pd.read_csv("E:/US/TSHIRT/linklabel_0911.csv")

print(list)
# list_url = []

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"
    }

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
    r = requests.get(url, headers=headers)
    filename = os.path.join("", url.split("/")[-1])
    with open(f"{list["ordercode"][i]}.pdf", "wb") as fd:
        fd.write(r.content)

