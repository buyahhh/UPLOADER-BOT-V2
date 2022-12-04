import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5917720957:AAGiYH_A7IabgHNpyMYsTHB3pdk0XZE6ta8")
    
    API_ID = int(os.environ.get("API_ID", 10682533))
    
    API_HASH = os.environ.get("API_HASH"41a93e59d8940968ba71e92a978e2fcb)
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "2027520982"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "")

    MAX_RESULTS = "50"
