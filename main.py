from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "BURAYA_DOKUNMA"  # Render bunu kullanmayacak

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Anime bot çalışıyor 🔥")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
