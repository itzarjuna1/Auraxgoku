import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

# Telegram API Configuration
API_ID = int(os.environ.get("API_ID", "22565342"))  # Your Telegram API ID
API_HASH = os.environ.get("API_HASH", "75e035926f72f2f4155a6f5f6e64be03")  # Your Telegram API HASH
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")  # Your Bot Token

# MongoDB Configuration
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Your MongoDB URI
MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "AURAMUSICBOT")  # Your MongoDB Name

# Bot Configuration
BOT_USERNAME = os.environ.get("BOT_USERNAME", "7931445226:AAGf8aP4uJxhdCNyfsa-RgQSRV8_-lXLoeY")  # Your Bot Username without @
SESSION_STRING = os.environ.get("SESSION_STRING", "BQFYUd4AkVjGeCzSGzqd7OdkMyLtZ373VPK5ZFihSAgdfuS7ccs-kfHSGE1Lz5yvvXQroBg9Q_XQfmTvHgllIRlcZBwNdB4OQjRQmspcMBa5gFQCWN_4Vw7lhsA-6Hanfts29gWEUAfWJj1Lt4sI29a7ufq9k4oPThym31akZQBscakrugQf-Ed2QwCnORyOzn8-nTzZaVRduBjldci1doBx0n1d8prsS2xLTm9gBbYWsnVfZePFE5l0OJbTSz62w7vLM0qQPMjS6FKXllxkcriO5Dc5RGsKGVwJ-boT0bUrOqM4fV3jB_WLsKiEG7bv4jA-O0zYBgH7LRwU2gi7EGvGjy8ZgQAAAAHQda6jAA")  # Pyrogram Session String (needed for userbot mode)

# Owner and Admins Configuration
OWNER_ID = int(os.environ.get("OWNER_ID", "7926944005"))  # Your Telegram User ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))  # Sudo Users List
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "https://t.me/dark_knight_support")  # Support Chat Username without @

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

