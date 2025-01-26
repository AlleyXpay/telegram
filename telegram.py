import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# Укажите ваш токен Telegram-бота
TOKEN = "7807468550:AAGPAvhicqongt3umf_pPVakjxyojPJK7eA"

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# URL на ваше веб-приложение (например, размещённое на GitHub Pages или другом хостинге)
WEBAPP_URL = "https://alleyxpay.github.io/Dia/"

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Кнопка с WebApp
    webapp_button = KeyboardButton("Играть", web_app=WebAppInfo(url=WEBAPP_URL))
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(webapp_button)

    bot.send_message(
        message.chat.id,
        "Привет! Нажми на кнопку \"Играть\", чтобы открыть игру.",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    bot.polling(none_stop=True)
