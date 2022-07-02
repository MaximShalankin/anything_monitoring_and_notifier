import os
from dotenv import load_dotenv
from notification_ways.notify_telegram import send_message_telegram_chat


load_dotenv()
TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')

__all__ = [
    # const variables
    'TG_BOT_TOKEN',

    # modules import ways to notify for future
    'send_message_telegram_chat',
]