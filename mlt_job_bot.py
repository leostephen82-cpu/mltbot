#!/usr/bin/env python3
"""
BSc MLT Government Vacancy Bot
------------------------------
Checks job feeds/pages for BSc MLT / Lab Technician government vacancies,
remembers what it has already seen, and alerts you only about NEW ones.

Setup:
    pip install requests feedparser beautifulsoup4

Optional Telegram alerts (recommended):
    export TELEGRAM_BOT_TOKEN="123456:ABC..."   # create via @BotFather
    export TELEGRAM_CHAT_ID="your_chat_id"      # get via @userinfobot

Run once:        python mlt_job_bot.py
Run every 3 hrs: python mlt_job_bot.py --loop 3
Or use cron / GitHub Actions to run it on a schedule.
"""

import argparse
import os
import re
import sqlite3
import time
from urllib.parse import quote_plus, urljoin

import feedparser
import requests
