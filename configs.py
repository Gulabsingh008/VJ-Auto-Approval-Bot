# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21784817"))
    API_HASH = getenv("API_HASH", "c8209405e82ac1d833e653d0330bbf17")
    BOT_TOKEN = getenv("BOT_TOKEN", "6564513574:7003534933:AAFexthFi2eV_OTZEtJZ1tqNjj3tzIdwpCU")
    FSUB = getenv("FSUB", "Ra_yan_2024_movie")
    CHID = int(getenv("CHID", "-1002172671575"))
    SUDO = list(map(int, getenv("SUDO", "1114789110").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
