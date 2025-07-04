import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "22565342",None))
API_HASH = getenv("API_HASH", "75e035926f72f2f4155a6f5f6e64be03",None)

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7931445226:AAGf8aP4uJxhdCNyfsa-RgQSRV8_-lXLoeY",None)

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",None)
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "aura x music",None)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002576326140",None))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7078181502"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/itzarjuna1/Auraxgoku.git",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/dark_x_knight_musiczz_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/dark_knight_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4"
)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION", "BQFYUd4AaBQ-7rxbKMguDsyH8oJPUtsDN4JBK4J-P09mTvQkHm24IsRuD3VtdQi1nbxvR97mcLHog1Ke9s6dKIYskILAyeaNzfr7CayVeDm_hiY0XKz9Ge7BR8A4KXBFdpUy_9KA7t0yDheKWcdJOM-ArBjs40uUUIjyPd0tntz3tWArfLmttWkuUNI2LGmTn_EjZjBH_XRopuZNVsesynDa7C5z8a-5V_Z87OKlzkoQL8u5Tw34EYMA_0eBsdjuEs5-rU2gz80eDSdIf9e0Pf7vWxy8tPxRjNe6DROsj5-m-CEys1SIoF_Uaw0jCZo8lZRRFk_ezLpnp2zclT0dk3iCxJDPeQAAAAHjZt-vAA",None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/t0t93h.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/lbl62s.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/ka4lzo.jpg"
STATS_IMG_URL = "https://files.catbox.moe/o82ph9.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/ka4lzo.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/lbl62s.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/t0t93h.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/o82ph9.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/o82ph9.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/ka4lzo.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/lbl62s.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/t0t93h.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
