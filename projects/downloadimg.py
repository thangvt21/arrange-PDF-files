import pandas as pd
import requests
import os

# Link Google Sheet đã được chia sẻ công khai (dưới dạng CSV)
#sheet_url = "https://docs.google.com/spreadsheets/d/1Q2r3XnDRarlS4CE2SInNRAbgh26FkH-f7MelegDZruo/edit?usp=sharing".replace('/edit#gid=', '/export?format=csv&gid=')

# Đọc dữ liệu từ Google Sheet
df = pd.read_csv(r"D:\work\Tool FlashPOD\Note Thư - 2222.csv")

# Tạo thư mục lưu ảnh nếu chưa tồn tại
os.makedirs('downloaded_images', exist_ok=True)

# Duyệt qua từng URL và tải ảnh
for index, row in df.iterrows():
    img_url = row[0]  # Giả sử URL ảnh ở cột A
    try:
        response = requests.get(img_url)
        response.raise_for_status()  # Kiểm tra lỗi HTTP

        # Lưu ảnh với tên dựa trên số thứ tự
        img_name = f"downloaded_images/{str(row[1])}.png"
        with open(img_name, 'wb') as f:
            f.write(response.content)

        print(f"Tải thành công: {img_name}")
    except Exception as e:
        print(f"Lỗi khi tải {img_url}: {e}")
