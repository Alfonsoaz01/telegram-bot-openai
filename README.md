# telegram-bot-openai

This project aims to create a Telegram bot using the OpenAI API.

## Configuration

There is an environment variable file called `.env` that contains the configuration for the bot. The file should contain the following variables:

```
AZURE_OPENAI_API_KEY=
API_TOKEN_TG=
OPENAI_MODEL=
OPENAI_ENDPOINT=
ALLOWED_ID_USER=
```

After setting the environment variables, the bot is ready to be used.

## Telegram

To obtain the telegram bot token, you need to create a new bot using the BotFather on Telegram. The OpenAI API key can be obtained by creating an account on the OpenAI website.

Check on the following link to obtain your id: https://www.alphr.com/telegram-find-user-id/

## Installation

There are two alternatives for installation:

1. Using Docker: Build the image and run the container.

   - To build the image, run the following command:
     ```bash
     docker build -t telegram-bot-openai .
     ```
   - Alternatively, you can use the docker-compose file:
     ```bash
     docker-compose up
     ```

2. Local installation: Run the bot directly on your machine.
   - Ensure Python 3.8 or higher is installed.
   - Install the dependencies using the following command:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the bot using the following command:
     ```bash
     python bot.py
     ```
