from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "34594672"))
API_HASH = getenv("API_HASH", "a008e5018b8662e872be5a8670db4840")

BOT_TOKEN = getenv("BOT_TOKEN", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "7651303468"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/d22cec7c75e26f36edff7-0ce8cae0037d4aa0aa.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/d22cec7c75e26f36edff7-0ce8cae0037d4aa0aa.jpg")

SESSION = getenv("SESSION", "")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/snowy_hometown")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/dark_musicgm")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8564072723").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
