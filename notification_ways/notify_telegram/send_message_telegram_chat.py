import telebot


def send_message_telegram(tg_bot_token, chat_id, message_text):
    bot = telebot.TeleBot(token=tg_bot_token)
    _ = bot.send_message(chat_id=chat_id, text=message_text)
