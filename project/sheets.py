import gspread
from google.oauth2.service_account import Credentials
from config import SPREADSHEET_NAME, SHEET_NAME

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)
sheet = client.open(SPREADSHEET_NAME).worksheet(SHEET_NAME)


def get_next_item():
    rows = sheet.get_all_records()

    for i, row in enumerate(rows, start=2):
        if row["status"] == "ready":
            return i, row

    return None, None


def mark_posted(row_index):
    sheet.update_cell(row_index, 5, "posted")
