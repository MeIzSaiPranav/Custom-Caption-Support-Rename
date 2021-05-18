import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_FILE_SIZE = 2097152000
    CHUNK_SIZE = 128
    DB_URI = os.environ.get("DATABASE_URL", "")
    CAPTION = os.environ.get("CAPTION", "")
    CHANNEL_NAME_1 = os.environ.get("CHANNEL_NAME_1", "CHANNEL 1")
    CHANNEL_ID_1 = int(os.environ.get("CHANNEL_ID_1", 12345))
    CHANNEL_NAME_2 = os.environ.get("CHANNEL_NAME_2", "CHANNEL 2")
    CHANNEL_ID_2 = int(os.environ.get("CHANNEL_ID_2", 12345))
    CHANNEL_NAME_3 = os.environ.get("CHANNEL_NAME_3", "CHANNEL 3")
    CHANNEL_ID_3 = int(os.environ.get("CHANNEL_ID_3", 12345))
    CHANNEL_NAME_4 = os.environ.get("CHANNEL_NAME_4", "CHANNEL 4")
    CHANNEL_ID_4 = int(os.environ.get("CHANNEL_ID_4", 12345))
    CHANNEL_NAME_5 = os.environ.get("CHANNEL_NAME_5", "CHANNEL 5")
    CHANNEL_ID_5 = int(os.environ.get("CHANNEL_ID_5", 12345))
    CHANNEL_NAME_6 = os.environ.get("CHANNEL_NAME_6", "CHANNEL 6")
    CHANNEL_ID_6 = int(os.environ.get("CHANNEL_ID_6", 12345))


