import os
from dotenv import load_dotenv
from openai import OpenAI
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters


load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


AI_INSTRUCTIONS = (
    "Ты полезный AI-ассистент. "
    "Обработай сообщение пользователя согласно задаче проекта."
)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    try:
        response = client.responses.create(
            model="gpt-5-mini",
            instructions=AI_INSTRUCTIONS,
            input=user_text
        )

        short_text = response.output_text
        await update.message.reply_text(short_text)

    except Exception as error:
        print("OpenAI error:", error)
        await update.message.reply_text(
            "⚠️ Не удалось обработать текст. Попробуйте ещё раз позже."
        )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я AI-бот.\n\n"
        "Отправь мне сообщение, и я обработаю его с помощью AI."
    )

app = Application.builder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot started...")
app.run_polling()