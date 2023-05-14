import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6097109946:AAFjPwiAwW0XRtJqj_TFNWgVF_PmWRjFcbE")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "6817364"))
    API_HASH = os.environ.get("API_HASH", "b2aea0b75ceca34bf5333107ac526c02")
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4194304000 #2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "887108671"))
    SESSION_NAME = "1ApWapzMBu3ovTJgp-xdmo-ujOni9vM7vShRpcLW609aJCmM0_y6NDbko5PEJm4vzVVavZX74fkKxbMnMyQMxEwX5W-hAjqjpW2u-miMryZSaYNY36Iu9nfd2yPJyYLet5yUhksCtMRL-0dvYjgpKX5xuhkXn-fQBY5QGvXR97IIh64mzkxXr6KlVq0skdTyoTZwiVafSnDXucoJLIFlhSiP3QrlaWS-9J2DFhjd35M_fj14xGeDWk60Lz8jLaevOQPS6hrQgCx8nJEGfi-XeWlRaJLWN52pKomu1Njm0wqaXgjgdFBFoQ38x24uOP5YNSqJ0UONTb9aLJ4eYVo57awmOfVY6LBk="
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://db-mongodb-ams3-25994-51438eff.mongo.ondigitalocean.com")
    MAX_RESULTS = "50"
    PREMIUM_USER = os.environ.get("io9868")
