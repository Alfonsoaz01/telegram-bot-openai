# telegram-bot-openai

This project aims to create a Telegram bot that uses the OpenAI API to summarize the content you send him.

## Configuration

There is an environment variable file called `.env` that contains the configuration for the bot. The file should contain the following variables:

```
AZURE_OPENAI_API_KEY=
API_TOKEN_TG=
OPENAI_MODEL=
OPENAI_ENDPOINT=
```

After setting the environment variables, the bot is ready to be used.

## Telegram

To obtain the telegram bot token, you need to create a new bot using the BotFather on Telegram. The OpenAI API key can be obtained by creating an account on the OpenAI website.

Check on the following link to obtain your id: https://www.alphr.com/telegram-find-user-id/
You need to insert the id in the `bot.py` file in the allowed_user_ids list.

## Installation

There are two alternatives for installation:

1. Using Docker: Build the image and run the container.

   - To build the image, run the following command:
     ```bash
     docker build -t telegram-bot-openai .
     ```
   - And run the container using the following command:
     ```bash
     docker run -d --env-file .env telegram-bot-openai
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

## Time spent on the project

I have built this project in an hour as a challenge to myself. The bot is not perfect, but it works. Feel free to contribute to the project. I would love to see your contributions.

## Support

Do you like this content? You can support me by buying me a coffee:
https://www.buymeacoffee.com/fonxoaz
