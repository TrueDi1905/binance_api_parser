from telegram import Bot

#данные указаны напрямую, без сокрытия, для удобства тестирования
#в любом другом случае прячем данные в .env
CHAT_ID = "672595973"
TELEGRAM_TOKEN = "5236192500:AAHRP8YYqc9cBSto4yFehUPJIsUoSdIdwqs"

bot_client = Bot(token=TELEGRAM_TOKEN)


async def send_message(message):
    return bot_client.send_message(chat_id=CHAT_ID, text=message)
