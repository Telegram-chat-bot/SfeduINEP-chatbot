import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.environ.get("TOKEN")
ADMIN_DATA = {
    "426499247": "860269"
}
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")
DP_HOST = os.environ.get("DB_HOST")
# print("426499247" in [k for k,v in ADMIN_DATA.items()])