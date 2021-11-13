from fake import fake
import telebot

bot = telebot.TeleBot(fake["fake"])

@bot.message_hendler(commands=[start])
def start_funk(massage) :
    bot.send_message(message.chat.id, "Как тебя зовут?")

@bot.message_handler(content_types=["text"])
def hello(message):
    msg.send_message(message.chat.id, "Привет" {message.text})
    # bot.register_next_step_handler(msg.name)
    
if __name__ == '__main__':
    bot.polling(none_stop=True)
