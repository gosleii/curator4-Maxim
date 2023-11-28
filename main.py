import telebot
bot = telebot.TeleBot('6511304838:AAFD2SSIKf5iSdyeaMwrVMYdbF8vQBlN6tk')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, text="Hello!!! You've visited MailBot. If you want to sign up wrtie '/sign' in the chat.")

@bot.message_handler(commands=['sign'])
def main(message):
    bot.send_message(message.chat.id, text="You succesfully signed up!!! Write '/get_link' if you want to visit our official site.")

@bot.message_handler(commands=['get_link'])
def main(message):
    bot.send_message(message.chat.id, 'ЭТО [ССЫЛКА](https://mail.ru/?ysclid=lpilhhz2yo4271651)')

bot.infinity_polling()