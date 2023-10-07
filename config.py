import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    BOT_TOKEN = os.getenv("6410671087:AAFxWyX8saGsMix6vsJBh16T84NRxb66WFY")
    SERVERLESS = os.getenv("SERVERLESS", "").lower() in ("yes", "y", "1", "true")
    WEBHOOK_HOST = os.getenv("https://11111-blush.vercel.app/updateWebhooks?token=6410671087:AAFxWyX8saGsMix6vsJBh16T84NRxb66WFY")
    PORT = int(os.getenv("PORT", 8000))
