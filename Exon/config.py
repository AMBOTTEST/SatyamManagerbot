"""
MIT License

Copyright (c) 2022 ABISHNOI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Abishnoi
#     MY ALL BOTS :- Abishnoi_bots
#     GITHUB :- KingAbishnoi ""

import json
import os


def get_user_list(config, key):
    with open("{}/Exon/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    API_ID = "12227067"
    API_HASH = "b463bedd791aa733ae2297e6520302fe"
    ARQ_API_KEY = "EJSUNZ-BJXKAI-AKQDZL-NMPKWQ-ARQ"
    BOT_ID = "6129232106"
    TOKEN = "5458182410:KINGABISHNOI-UM"
    OWNER_ID = "6204761408"
    OPENWEATHERMAP_ID = "22322"
    OWNER_USERNAME = "AM_YTBOTT"
    BOT_USERNAME = "Defulter_bot"
    SUPPORT_CHAT = "AM_YTSUPPORT"
    UPDATES_CHANNEL = "satyamnetwork"
    SUPPORT_CHANNEL = "AM_YTSUPPORT"
    JOIN_LOGGER = "-1001841879487"
    EVENT_LOGS = "-1001908711819"
    ERROR_LOGS = "-1001840241140"

    SQLALCHEMY_DATABASE_URI = "postgres://citus:AbhiModszYT12@c-yone.2iti2yet5lss6l.postgres.cosmos.azure.com:5432/yone"  # sql
    DATABASH_URL = "postgres://citus:AbhiModszYT12@c-yone.2iti2yet5lss6l.postgres.cosmos.azure.com:5432/yone"  # sql
    DB_URL = "postgres://citus:AbhiModszYT12@c-yone.2iti2yet5lss6l.postgres.cosmos.azure.com:5432/yone"
    MONGO_DB_URL = "mongodb+srv://AM:AM@am.9zeddhx.mongodb.net/?retryWrites=true&w=majority"  # needed for any database modules
    MONGO_URL = "mongodb+srv://AM:AM@am.9zeddhx.mongodb.net/?retryWrites=true&w=majority"
    DB_URL2 = "mongodb+srv://AM:AM@am.9zeddhx.mongodb.net/?retryWrites=true&w=majority"  # YOUR MONGO_DB_URI
    ARQ_API_URL = "https://arq.hamker.in"
    BOT_API_URL = "https://api.telegram.org/bot"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "RcTrglJSXxi6I~5Rr4NLwVOWeVWEzhh7e6MiIqURbhe~3brOGAN4nCSo93bqXSpa"
    SPAMWATCH_SUPPORT_CHAT = "@AM_YTSUPPORT"

    REDIS_URL = "redis://default:725m47dhlmisA0QecURSMkcHNGXkM1uP@redis-15808.c275.us-east-1-4.ec2.cloud.redislabs.com:15808"

    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    REQUESTER = get_user_list("elevated_users.json", "whitelists")
    DEMONS = get_user_list("elevated_users.json", "supports")
    INSPECTOR = get_user_list("elevated_users.json", "sudos")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    DONATION_LINK = "https://t.me/AM_YTBOTT"
    CERT_PATH = None
    STRICT_GBAN = "True"
    PORT = ""
    DEL_CMDS = "True"
    STRICT_GBAN = "True"
    WORKERS = 8
    BAN_STICKER = ""
    ALLOW_EXCL = True
    CASH_API_KEY = "PNNU99H3W9KDLKVM"
    TIME_API_KEY = "9HK7J0H25AKQ"
    WALL_API = "F-OFF"
    AI_API_KEY = "LOVEYOU"
    BL_CHATS = []
    SPAMMERS = True
    SPAMWATCH_API = ""
    ALLOW_CHATS = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
    REM_BG_API_KEY = "E1xSqCSNqapeV9qi5mpxLgTa"
    LASTFM_API_KEY = "FMLODA"
    CF_API_KEY = "KISS"
    BL_CHATS = []
    MONGO_PORT = "27017"
    MONGO_DB = "EXON"
    PHOTO = "https://graph.org/file/cbf13f8c3a437d7c4a940.jpg"
    HELP_IMG = "https://graph.org/file/cbf13f8c3a437d7c4a940.jpg"
    START_IMG = "https://graph.org/file/cbf13f8c3a437d7c4a940.jpg"
    TIME_API_KEY = "5LB4TAKPEKZ0"
    INFOPIC = False
    GENIUS_API_TOKEN = "wTqx6KCc1yMGLCeNwyRz9B6_ej8Qk1JHjeePf26mqtUWQi1hdzSxNkR-gP_z4-RL"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True


# ENJOY
