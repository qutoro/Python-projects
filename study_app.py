from google import genai
import telebot

client = genai.Client(api_key="AIzaSyDTfCnUOeDNd3837tqr5DnKUWIZonO3MfE")
bot = telebot.TeleBot("8010832936:AAH1h7foneBmhRdNP2C8a5I_-B_N83isI2Q")

user_history = {}


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я AI бот.\n\n"
        "/ask - задать вопрос\n"
        "/learn - получить обучающий материал\n"
        "/clear - очистить историю диалога"
    )


# очистка памяти
@bot.message_handler(commands=["clear"])
def clear_history(message):
    user_history[message.chat.id] = []
    bot.send_message(message.chat.id, "История диалога очищена.")


# обучающий режим
@bot.message_handler(commands=["learn"])
def learn_mode(message):

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Объясни тему простыми словами: {message.text}"
    )

    bot.send_message(message.chat.id, " Обучающий материал:\n\n" + response.text)


@bot.message_handler(commands=["ask"])
def ask(message):

    bot.send_message(message.chat.id, "Напиши свой вопрос.")


@bot.message_handler(func=lambda message: True)
def chat(message):

    try:

        chat_id = message.chat.id

        if chat_id not in user_history:
            user_history[chat_id] = []

        # добавляем сообщение пользователя
        user_history[chat_id].append(f"User: {message.text}")

        # берем последние 6 сообщений
        context = "\n".join(user_history[chat_id][-6:])

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=context
        )

        answer = response.text

        # сохраняем ответ
        user_history[chat_id].append(f"Bot: {answer}")

        bot.send_message(chat_id, answer)

    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")


bot.infinity_polling()
