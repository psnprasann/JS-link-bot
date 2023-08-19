# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "18332041"))
API_HASH = os.environ.get("API_HASH", "25a2fdd87318e028812a6826a428a4c1")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6238576785:AAHFRndDOOPdCJa7TLh9FAAZXS7uBW03_yU")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("15415755")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "JayRaj8833")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://jayraj8833:jayraj8833@jayraj8833.nvvpbu7.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5810492729")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1782059495)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-951607810")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "LnThamizha_007") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://i.ibb.co/D1YNsyp/IMG-20230820-021503-579.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
