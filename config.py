import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "16841147"))
API_HASH = getenv("API_HASH", "724367ca3534a7e37594fcf3512dc8ad")

BOT_TOKEN = getenv("BOT_TOKEN", "5861787158:AAFSeyWt9y2wiOKZH4CMm0Jw8WSn0ffXuuI")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://unk0:unk@cluster0.05tiqap.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001632249971"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "UNK")

OWNER_ID = list(map(int, getenv("OWNER_ID", "1211015395").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://t.me/UNK_BOTS")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/UNK_BOTS")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/UNK_SUPPORT")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "AQAn992sVieKPRMlAoDOHbz4JvUdvrS4MIWkEfhga6II5KP7VCIvRdL6RlSa82atSfPnFl5Fr_2waH-E1FndLDBCB6PDcj8QpQmdxlSkwiVDMeIaRmoXbA6hDjzNJk1SGw8-KL2HsyhIeE_yJSNOf-YNYmDWRQ192AAzcvu5HJFKc7-CSALgOZ4PZ1nBbdr08caqv4eeodV8xrQ4basAbFyxhcaFB19ufz1QaCoVh2f_r9pFvqiUtSSctHhBOFEsm_Jy0dFHorgja2cfyg_8-fgZiNxp9BMhPbP4bBcBq0ZYiVMAUOfG-9PKrQgNUcyeTCPv19c0wySJH9Xbs4azmbtxAAAAAVTfy7wA")
STRING2 = getenv("STRING_SESSION2", "AQBjSo44WOn6LTwCy-qxeWNk46k_8bpnfk5cNiIG5kdLFWXM5KG8y_ILY5H_aNppHjhyLbyEq-ci27UaCfW-I9fwFsAaIG3Sfwdk9YiwUP-KNBiB57NecN_8ZtKd8vXYVhw0CuryL8HgtAr-RZ0HPVZ62LNoQo2srBwk_3ga3xoCYUCZdC8sywglK9aZDkNTCsak8LTHqoDo14IqrD1VUpHNP8haIWQBXnjkpn_GiTx8v2jP9AuINB3Dsz7f8iR2KfOafhBAPmEweLD9zC-vsfSomG04-qOx2En2hfl4NVroJD0vfclGmUd-yu3dSB7T5q_qXQ9EO3bvGhlF1dm1AAAAAWRrrHMA")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/99f94a2836f6449731377.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/c8275dc095ebd6312466a.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/64db0bafe7d274e642932.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/b491af30bb38f791d75eb.jpg"

STATS_IMG_URL = "https://telegra.ph/file/2ecbe22409921e0e09012.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "httphttps://telegra.ph/file/c8275dc095ebd6312466a.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/99f94a2836f6449731377.jpg"
