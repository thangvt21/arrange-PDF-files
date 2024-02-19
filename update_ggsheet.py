import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

credentials = Credentials.from_service_account_file(
    "E:/THANGVT/tools/arranger_v2.2/arrange-PDF-files/luminous-lodge-321503-2defcccdcd2d.json",
    scopes=scopes,
)

gc = gspread.authorize(credentials)

sh = gc.open("Machine 2")
