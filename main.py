import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.getenv("8697906484:AAHTbLwxTFdw1QpxmcMeTIQy7RPe_3G87Rg")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🚀 Бесплатный VPN-Сервис

🔒 Быстрый и безопасный интернет:

✅ 50 ГБ каждый месяц
✅ Дешевая премиум подписка
✅ Красивый интерфейс
✅ Стабильное подключение

📱 Скачать:
https://play.google.com/store/apps/details?id=okovpn.app
"""

    keyboard = [
        [
            InlineKeyboardButton(
                "📥 Скачать VPN",
                url="https://play.google.com/store/apps/details?id=okovpn.app"
            )
        ],
        [
            InlineKeyboardButton(
                "🌐 Наш сайт",
                url="ТВОЯ_ССЫЛКА_RENDER"
            )
        ]
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
