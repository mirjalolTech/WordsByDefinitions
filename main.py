import requests
import uuid # Import uuid for generating unique IDs
import os # Import os for environment variables
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent # Import InlineQueryResultArticle
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler, InlineQueryHandler # Import InlineQueryHandler

BOT_TOKEN = os.getenv("BOT_TOKEN") # Get token from environment variable
# Check if BOT_TOKEN is set
if not BOT_TOKEN:
    print("Error: BOT_TOKEN environment variable not set. Please set it before running the bot.")
    exit()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am a dictionary bot. Send me any word to get its definition.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """🚨If you need any help, you can contact admin: @EnglishDictionaryHelper

💻If you want to advertise your product, contact with the owner: @mirjalolvalijonov"""
    await update.message.reply_text(help_text)

async def get_definition_text(word: str) -> str:
    """Helper function to fetch and format definition."""
    try:
        r = requests.get(f"https://dictionary-api.eliaschen.dev/api/dictionary/en/{word}", timeout=10)
        r.raise_for_status()
        data = r.json()

        text = f"📖 {data['word']}\n\n"
        if data.get("pronunciation"):
            text += f"🔊 {data['pronunciation'][0]['pron']}\n\n"
        for d in data.get("definition", [])[:2]:
            text += f"({d['pos']}) {d['text']}\n\n"

        return text.strip()

    except Exception:
        return "❌ Word not found."

async def define(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word = update.message.text.strip().lower()
    if not word or word.startswith("/"):
        return

    definition_text = await get_definition_text(word)
    await update.message.reply_text(definition_text)

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return

    definition_text = await get_definition_text(query)
    results = [
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title=f"Define {query}",
            input_message_content=InputTextMessageContent(definition_text)
        )
    ]
    await update.inline_query.answer(results)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, define))
    app.add_handler(InlineQueryHandler(inline_query))

    app.run_polling()

if __name__ == '__main__':
    main()
