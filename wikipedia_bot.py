import telebot
from googlesearch import search


TOKEN = "7560667603:AAFgqbxopYEdMxqi4TbkLcb4f-wkQnOpi3o"

# usar token del bot de Telegram
bot = telebot.TeleBot(TOKEN) 
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hola, soy un bot de Wikipedia. Envíame un término y te daré información al respecto.")


@bot.message_handler(content_types=['text'])
def help(message):
    bot.send_message(message.chat.id, "Envíame un término y te proporcionaré información de Wikipedia sobre él.")
    bot.register_next_step_handler(message, answering)

def answering(message):
    try:
        malas_palabras = ["porno", "violencia", "odio", "terrorismo", "racismo"]
        if any(palabra in message.text.lower() for palabra in malas_palabras):
            bot.reply_to(message, "Lo siento, no puedo proporcionar información sobre ese tema.")
            return
        busqueda = message.text 
        resultados = search(busqueda, num_results = 10, lang="es")
        bot.reply_to(message, "Aquí tienes algunos resultados de búsqueda:\n")
        for resultado in resultados:
            bot.send_message(message.chat.id, resultado)

    except Exception as e:
        bot.reply_to(message, f"Lo siento, no pude encontrar información sobre ese término. Intenta con otro: {e}")

bot.infinity_polling()