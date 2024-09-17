import os
import logging
from logging.handlers import RotatingFileHandler

# Retrieve sensitive information from environment variables
TG_BOT_TOKEN = os.environ.get("7441304802:AAGrjVdrmh4bzJOK_FloV2zgrwil6RyW80Q")
APP_ID = int(os.environ.get("20733274"))
API_HASH = os.environ.get("a74c1ddba4508413caf9bf608ac8d9e1")
CHANNEL_ID = int(os.environ.get("-1002027094726"))
OWNER_ID = int(os.environ.get("7109918450"))

# Check for missing sensitive data
if not all([TG_BOT_TOKEN, APP_ID, API_HASH, CHANNEL_ID, OWNER_ID]):
    raise ValueError("Missing required environment variables.")

# Port and database configuration
PORT = os.environ.get("PORT", "8080")
DB_URI = os.environ.get("mongodb+srv://vikas:vikas@vikas.yfezexk.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

# Ensure database URI is provided
if not DB_URI:
    raise ValueError("Missing DATABASE_URL environment variable.")

# Custom messages
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from a special link.")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join my Channel/Group to use me\n\nKindly Please join Channel</b>")
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION")
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") == "True"
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON") == 'True'

# Admins configuration
ADMINS = [OWNER_ID, 6574393060, 7109918450]  # Added new admin ID here

# Logging setup
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
