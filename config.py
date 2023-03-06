
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6239376376:AAEdXvJyycIpYBUXJafw18hAzPYkIUNrmmo")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "23068172"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "0192fd3730b181af037274f8d718c479")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQBL_7vLQ-oeHvtxPwwhBE-OJ6ceChhZxGfoNgAZ04-w_t4k4_xLyFtxQEc9BTChPK1u2HitANMpExt8elzVa5u1f10GlhluRS5AOFDE-fimKg0YJPJsOEWEXpJSDhR2DMF6pAD8XfIoQhwPYopRdc48Irtpn4YhEo8oRBltdI_fXXhalq3maiYK-iVyFMQKnA07o6pa_XiLbv9dBK2gYydAIK6G7mgcAZjtqId6DiX2wceEXn5tVHrWgLYSxZnrhQTKhnzACvk_Nj0vh-zmlSP0UZkiMpLTp16yVa661bxSapk5-z-YqJb4c5VH4eOrZIRNfSOF9hR_wVbErd_eyOpxcFyK4wA")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1001850269560")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
