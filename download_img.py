from datetime import date
import urllib
import pandas as pd
import os
import urllib.request
from tqdm import tqdm
import requests

# Create Opener prevent 403 Forbidden
opener = urllib.request.build_opener()
opener.addheaders = [
    (
        "User-Agent",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36",
    )
]
urllib.request.install_opener(opener)


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


# Import CSV file contains Order's List image URLs, delete duplicates (url)
def importCSV(filename):
    df = pd.read_csv(filename + ".csv")
    df.drop_duplicates()
    urls = df.values.tolist()
    return urls


# Download and save image files to folder
def downloadImg(urls, dir, filename):
    response = requests.get(urls)
    filepath = os.path.join(dir, filename)
    with open(filepath, "wb") as f:
        f.write(response.content)


# Main
def main():
    dir = "E:/THANGVT/tools/arranger_v2.2/arrange-PDF-files/download"
    p = input("ten file: ")
    urls = importCSV(p)
    i = 0
    for link in urls:
        url = "".join(link)
        filename = f"file{i}"
        i += 1
        downloadImg(url, dir, filename)


main()
