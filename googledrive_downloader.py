import sys
import requests


def download_files(id, des):
    url = "https://drive.google.com/uc?export=download&confirm=1"
    session = requests.Session()
    reponse = session.get(url, params={"id": id}, stream=True)
    token = get_confirm_token(reponse)
    if token:
        params = {"id": id, "confirm": 1}
        response = session.get(url, params=params, stream=True)
    save_response_content(reponse, des)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            return value
    return None


def save_response_content(response, des):
    CHUNK_SIZE = 32768
    with open(des, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)


def main():
    if len(sys.argv) >= 3:
        file_id = sys.argv[1]
        des = sys.argv[2]
    else:
        file_id = "EMPTY ID"
        des = "EMPTY PATH"
    print(f"download {file_id} to {des}")
    download_files(file_id, des)


if __name__ == "__main__":
    main()
