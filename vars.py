#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23761741"))
API_HASH = environ.get("API_HASH", "065c3bcc3665622db237f65a9a5b47e4")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "7627244591"))
CREDIT = "❖❀～ ᴍᴀᴀꜰɪᴀ ᴍᴜɴᴅᴇᴇʀ ～❀❖"
AUTH_USER = os.environ.get('AUTH_USERS', '7627244591').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
