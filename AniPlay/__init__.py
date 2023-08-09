from os import environ
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(environ.get("APP_ID", "25695562")),
    api_hash= environ.get("API_HASH", "0b691c3e86603a7e34aae0b5927d725a"),
    bot_token= environ.get("TOKEN", "6105757517:AAEi2v-Y1B7GAiR50ED-3qfyoz4ymKLpjo8")
)
