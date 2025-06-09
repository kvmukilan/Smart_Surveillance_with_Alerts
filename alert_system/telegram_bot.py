import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from utils.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, LOG_CSV, SNAPSHOT_DIR
import pandas as pd
import asyncio
import nest_asyncio

nest_asyncio.apply() =


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👍 SmartSurv Bot active! Send /status to get recent events.")


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not os.path.exists(LOG_CSV):
        return await update.message.reply_text("No motion events yet.")
    df = pd.read_csv(LOG_CSV)
    last = df.tail(5)
    msgs = [f"{row['timestamp']} → {row['filename']}" for _, row in last.iterrows()]
    await update.message.reply_text("\n".join(msgs))

    for _, row in last.iterrows():
        path = os.path.join(SNAPSHOT_DIR, row['filename'])
        if os.path.exists(path):
            with open(path, 'rb') as img:
                await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)


def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    print("🤖 Telegram bot is running. Send /start or /status in chat.")
    
    # ✅ Avoid printing bot.id before it's initialized
    # ❌ Do NOT try to log app.bot.id before `app.initialize()`

    import asyncio
    import nest_asyncio
    nest_asyncio.apply()

    loop = asyncio.get_event_loop()
    loop.create_task(app.run_polling(close_loop=False))
    loop.run_forever()


if __name__ == "__main__":
    run_bot()
