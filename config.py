import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

# Telegram API Configuration
API_ID = int(os.environ.get("API_ID", 12345))  # Your Telegram API ID
API_HASH = os.environ.get("API_HASH", "")  # Your Telegram API HASH
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")  # Your Bot Token

# MongoDB Configuration
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "")  # Your MongoDB URI
MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "TuneViaBot")  # Your MongoDB Name

# Bot Configuration
BOT_USERNAME = os.environ.get("BOT_USERNAME", "")  # Your Bot Username without @
SESSION_STRING = os.environ.get("SESSION_STRING", "")  # Pyrogram Session String (needed for userbot mode)

# Owner and Admins Configuration
OWNER_ID = int(os.environ.get("OWNER_ID", 123456789))  # Your Telegram User ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))  # Sudo Users List
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "")  # Support Chat Username without @

# Bot Limits Configuration
MAX_QUEUE_SIZE = int(os.environ.get("MAX_QUEUE_SIZE", 50))  # Maximum songs in queue
MAX_PLAYLIST_SIZE = int(os.environ.get("MAX_PLAYLIST_SIZE", 20))  # Maximum playlist size
DURATION_LIMIT = int(os.environ.get("DURATION_LIMIT", 1800))  # Maximum song duration in seconds

# Command Prefixes
COMMAND_PREFIXES = os.environ.get("COMMAND_PREFIXES", "/ !").split()

# Log Channel Configuration
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", -100))  # Your Log Channel ID

# Debug Mode
DEBUG = bool(os.environ.get("DEBUG", False))

# Don't Edit Below This Line
class Config:
    API_ID = API_ID
    API_HASH = API_HASH
    BOT_TOKEN = BOT_TOKEN
    MONGO_DB_URI = MONGO_DB_URI
    MONGO_DB_NAME = MONGO_DB_NAME
    BOT_USERNAME = BOT_USERNAME
    SESSION_STRING = SESSION_STRING
    OWNER_ID = OWNER_ID
    SUDO_USERS = SUDO_USERS
    SUPPORT_CHAT = SUPPORT_CHAT
    MAX_QUEUE_SIZE = MAX_QUEUE_SIZE
    MAX_PLAYLIST_SIZE = MAX_PLAYLIST_SIZE
    DURATION_LIMIT = DURATION_LIMIT
    COMMAND_PREFIXES = COMMAND_PREFIXES
    LOG_CHANNEL_ID = LOG_CHANNEL_ID
    DEBUG = DEBUG

