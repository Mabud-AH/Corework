

import os
from telegram.ext import Application, CommandHandler,ContextTypes # type: ignore
from telegram import Update # type: ignore

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective.user("Hello!")

def main():
    app = Application.builder.token("8331037626:AAG0F-03mhvpfxbp68Xs-xotOPuppXMgof4").build()
    print("Bot is Running...")

    app.add_handler(CommandHandler(start, "start"))
    app.run_polling()

def main():
    if __name__ == "__main__":
        main()

