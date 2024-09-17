#(©)CodeXBotz




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

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7441304802:AAGrjVdrmh4bzJOK_FloV2zgrwil6RyW80Q")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20733274"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a74c1ddba4508413caf9bf608ac8d9e1")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002308411836"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7109918450"))

#Port
# Port and database configuration
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://vikas:vikas@vikas.yfezexk.mongodb.net/?retryWrites=true&w=majority")
DB_URI = os.environ.get("mongodb+srv://vikas:vikas@vikas.yfezexk.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002027094726"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")
# Ensure database URI is provided
if not DB_URI:
    raise ValueError("Missing DATABASE_URL environment variable.")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
# Custom messages
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from a special link.")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join my Channel/Group to use me\n\nKindly Please join Channel</b>")
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION")
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") == "True"
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON") == 'True'

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(6919672033,)
# Admins configuration
ADMINS = [OWNER_ID, 6574393060, 7109918450]  # Added new admin ID here

# Logging setup
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',

handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
