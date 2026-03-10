from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8631262698:AAF3uav7gCSQWZ0cQe-L0-I_GL0cTYo132o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    dashboard = """
📊 TRADING GUARDIAN OVERVIEW

Balance: $0.00 USDT
Portfolio Value: $0.00
Today's PNL: 0%

Open Positions: 0
Mode: TESTNET
Frequency: MEDIUM
Trading Style: MANUAL

Market Status: 🟢 Bullish
Last Update: now

Top 4 Prices
BTC: loading...
ETH: loading...
SOL: loading...
BNB: loading...
"""

    keyboard = [
        [InlineKeyboardButton("MODE", callback_data="mode"),
         InlineKeyboardButton("FREQUENCY", callback_data="frequency")],
        [InlineKeyboardButton("HISTORY", callback_data="history"),
         InlineKeyboardButton("TRADE STYLE", callback_data="style")],
        [InlineKeyboardButton("ACTIVE TRADES", callback_data="trades"),
         InlineKeyboardButton("SETTINGS", callback_data="settings")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(dashboard, reply_markup=reply_markup)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
