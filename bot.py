from telegram.ext import Updater, MessageHandler, Filters

# Tu token de Telegram
TOKEN = '6294129094:AAE-k3k6sHzz92YvHW7o4XeL1RIg4bKA-DI'

# Crear un objeto Updater
updater = Updater(token='6294129094:AAE-k3k6sHzz92YvHW7o4XeL1RIg4bKA-DI', use_context=True)

# Obtener el objeto dispatcher para registrar los controladores
dispatcher = updater.dispatcher

import openai
openai.api_key = "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"

def chat_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5,
    )
    message = response.choices[0].text
    return message.strip()

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola! Soy un bot de chat alimentado por OpenAI. ¿En qué puedo ayudarte?")

def reply(update, context):
    message = update.message.text
    response = chat_gpt(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

updater = Updater(token="6294129094:AAE-k3k6sHzz92YvHW7o4XeL1RIg4bKA-DI", use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
reply_handler = MessageHandler(Filters.text & (~Filters.command), reply)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(reply_handler)

updater.start_polling()
