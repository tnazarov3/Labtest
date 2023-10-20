import telebot
from telebot import types
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo

#bot = telebot.TeleBot('6362714649:AAEOjpU0NL6pu_DypST1JLIybi9U_WvxVMM')

web_app = WebAppInfo(url="https://tnazarov3.github.io/Labtest")

@bot.message_handler(content_types="web_app_data") #получаем отправленные данные 
def answer(webAppMes):
   print(webAppMes) #вся информация о сообщении
   print(webAppMes.web_app_data.data) #конкретно то что мы передали в бота
   bot.send_message(webAppMes.chat.id, f"получили инофрмацию из веб-приложения: {webAppMes.web_app_data.data}") 
   #отправляем сообщение в ответ на отправку данных из веб-приложения 



bot.polling(none_stop=True, interval=0)
