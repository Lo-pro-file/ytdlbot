#!/usr/local/bin/python3
# coding: utf-8

# ytdlbot - config.py
# 8/28/21 15:01
#

__author__ = "Benny <benny.think@gmail.com>"

import os

# general settings
WORKERS: "int" = int(os.getenv("WORKERS", 100))
PYRO_WORKERS: "int" = int(os.getenv("PYRO_WORKERS", 100))
APP_ID: "int" = int(os.getenv("APP_ID", 7234399))
APP_HASH = os.getenv("APP_HASH", "1c521005e55c95e6973ae714d2e9e424")
TOKEN = os.getenv("TOKEN", "5666045488:AAFyKF4tvzI0D0xVtPYR3x1dHZHSEqM0KAs")

REDIS = os.getenv("REDIS")

# quota settings
QUOTA = int(os.getenv("QUOTA", 5 * 1024 * 1024 * 1024))  # 5G
if os.uname().sysname == "Darwin":
    QUOTA = 10 * 1024 * 1024  # 10M

TG_MAX_SIZE = 2 * 1024 * 1024 * 1024 * 0.99
# TG_MAX_SIZE = 10 * 1024 * 1024

EX = os.getenv("EX", 24 * 3600)
MULTIPLY = os.getenv("MULTIPLY", 5)  # VIP1 is 5*5-25G, VIP2 is 50G
USD2CNY = os.getenv("USD2CNY", 6)  # $5 --> ¥30

ENABLE_VIP = os.getenv("", False)
MAX_DURATION = int(os.getenv("MAX_DURATION", 60))
AFD_LINK = os.getenv("", "")
COFFEE_LINK = os.getenv("", "")
COFFEE_TOKEN = os.getenv("")
AFD_TOKEN = os.getenv("")
AFD_USER_ID = os.getenv("")
OWNER = os.getenv("OWNER", "Opleech")

# limitation settings
AUTHORIZED_USER: "str" = os.getenv("AUTHORIZED_USER", "-1001829666524")
# membership requires: the format could be username/chat_id of channel or group
REQUIRED_MEMBERSHIP: "str" = os.getenv("REQUIRED_MEMBERSHIP", "-1001829666524")

# celery related
ENABLE_CELERY = os.getenv("ENABLE_CELERY", False)
ENABLE_QUEUE = os.getenv("ENABLE_QUEUE", False)
BROKER = os.getenv("BROKER", f"redis://{REDIS}:6379/4")

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASS = os.getenv("MYSQL_PASS", "root")

AUDIO_FORMAT = os.getenv("AUDIO_FORMAT")
ARCHIVE_ID = os.getenv("ARCHIVE_ID")

IPv6 = os.getenv("IPv6", False)
ENABLE_FFMPEG = os.getenv("ENABLE_FFMPEG", False)
RATE = float(os.getenv("RATE", 60 * 5))
BURST = int(os.getenv("BURST", 3))
