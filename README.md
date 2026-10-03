# Telegram AI Bot Template

A reusable Telegram bot template built with Python and the OpenAI API.

Use this project as a starting point for different Telegram AI bots, such as:

- AI assistants
- Text translators
- Customer support bots
- Lead qualification bots
- Text analysis tools
- Content generation bots
- Simple automation bots

## Features

- Receives text messages from Telegram
- Sends user messages to the OpenAI API
- Returns AI-generated responses back to Telegram
- Supports the `/start` command
- Handles OpenAI API errors
- Stores API keys in environment variables
- Can be adapted quickly for different client requirements

## Technologies

- Python
- Telegram Bot API
- OpenAI API
- python-telegram-bot
- python-dotenv

## Project Structure

- `bot.py` — main bot logic
- `.env` — API keys
- `.gitignore` — prevents secret files from being uploaded to GitHub
- `requirements.txt` — Python dependencies
- `README.md` — English documentation
- `README_RU.md` — Russian documentation

## Setup

1. Install the required dependencies:

`pip install -r requirements.txt`

2. Create a `.env` file.

3. Add your API keys:

`TELEGRAM_TOKEN=your_telegram_token`

`OPENAI_API_KEY=your_openai_api_key`

4. Open `bot.py`.

5. Change the `AI_INSTRUCTIONS` variable to match the task of the new project.

Example:

`AI_INSTRUCTIONS = "Translate the user's message into English."`

6. Update the `/start` message if needed.

7. Run the bot:

`python bot.py`

## How to Adapt the Template

For most new projects, the main things to change are:

1. `AI_INSTRUCTIONS`
2. `/start` message
3. Additional validation or business logic if required
4. Extra commands or integrations if the client needs them

The Telegram and OpenAI connection can usually stay the same.

## Security

Never upload real API keys to GitHub.

Store them in `.env`.

Make sure `.env` is included in `.gitignore`.

## Workflow

Telegram user → Python bot → OpenAI API → AI response → Telegram user