import telebot

from openai import AzureOpenAI
from dotenv import load_dotenv
import os 
import logging




# Cargar las variables de entorno desde el archivo .env
load_dotenv()

logging.basicConfig(filename='app.log', level=logging.DEBUG)



bot = telebot.TeleBot(os.environ['API_TOKEN_TG'])

allowed_user_ids = [os.environ['ALLOWED_ID_USER']]  # ID users allowed




def is_user_allowed(user_id):
    return user_id in allowed_user_ids


   

def create_response(text):
    try:
        client = AzureOpenAI(
            api_version="2023-07-01-preview",
            azure_endpoint=os.environ['OPENAI_ENDPOINT'],
        )

        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an assistant that helps summarize the content of long texts, so that users can read it in a faster and easier way. You can translate texts to Spanish if they are not in Spanish. You can summarize the texts in a way that they are shorter and easier to read."},
                {"role": "user", "content": f"Can you please summarize the content of the following text? I would need it to be summarized in English. If the original text is not in English, please translate it as best as possible and summarize it in a way that it retains the key points of the text and always has less summarized content than the original. Text content: {text}"}
            ],
            model=os.environ['OPENAI_MODEL'],
        )
        content = response.choices[0].message.content
        return content

    except Exception as e:
        print(f"Error generating answer: {e}")
        return None



@bot.message_handler(commands=['start', 'START'])
def send_welcome(message):
    if is_user_allowed(message.from_user.id):
        bot.reply_to(message, "Initialized bot, ready to summarize texts. Please send me a text to summarize.")
    else:
        bot.reply_to(message, "User not authorized to use the bot.")

        





@bot.message_handler(func=lambda message: is_user_allowed(message.from_user.id))
def echo_all(message):
    bot.send_chat_action(chat_id=message.chat.id, action="typing")
    try:
        response = create_response(message.text)
        bot.reply_to(message, "Resuming the content: \n\n" + response)
    except Exception as e:
        bot.reply_to(message, "Error")
    


bot.polling()
