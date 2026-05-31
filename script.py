from telebot import*
from time import sleep
from threading import*
water = 0
timer = False
token = "8010832936:AAGQlweorTQGGf--J2xWfagOqNA7HnN65ZM"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Команды:\n/setreminder 2 \n /drunk 200 \n /help \n /status")
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "после того как попили напишите /drunk и сколько выпили "+
                                      "штобы посмотреть сколько осталось напишите /status "+
                                      "норма 2л воды будет ситаться от двух литров")
@bot.message_handler(commands=['status'])
def send_status(message):
    if water <2000:
      bot.send_message(message.chat.id,f"Выпито уже {water} мл осталось {2000-water}" )
    else:
        bot.send_message(message.chat.id, f"Молодец ты законил дневную норму ты выпил {water} на {water - 2000} больше" )
@bot.message_handler(commands=['setreminder'])
def send_reminder(message):
    global timer
    try:
        timer = True
        hours = int(message.text.split()[1])
        bot.send_message(message.chat.id,"Напоминание поставлено")
        def StartTimer():
            time.sleep(3600*hours)
            if timer:
                bot.send_message(message.chat.id,"Пора пить воду")
        threading.Thread(target=StartTimer).start()
    except:
        bot.send_message(message.chat.id,"Пиши вот так /setreminder 2")
@bot.message_handler(commands=['drunk'])
def send_drunk(message):
    global water
    try:
        hours = int(message.text.split()[1])
        water += hours
        bot.send_message(message.chat.id, f"Выпито {water}")
    except:
        bot.send_message(message.chat.id,"Пиши вот так /drunk 200")

bot.polling()







