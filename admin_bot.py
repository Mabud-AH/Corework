import os
from dotenv import load_dotenv # type: ignore
from telegram import Update # type: ignore
from telegram.ext import Application, CommandHandler, ContextTypes # type: ignore
import datetime 
import jdatetime # type: ignore

# Load environment variables
load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.effective_user
        now = datetime.datetime.now()
        
        # Persian (Shamsi) date
        jdate = jdatetime.datetime.now()
        persian_date = jdate.strftime("%A, %d %B %Y")
        
        # Imperial Iranian date (requires manual calculation)
        imperial_year = jdate.year + 1180
        imperial_date = f"{jdate.strftime('%d %B')} {imperial_year}"
        
        # Gregorian date
        gregorian_date = now.strftime("%A, %d %B %Y")
        
        # Tehran time (UTC+3:30)
        tehran_time = (now + datetime.timedelta(hours=3.5)).strftime("%H:%M:%S")
        
        # UTC time
        utc_time = now.utcnow().strftime("%H:%M:%S")
        
        # Epoch time
        epoch_days = int(now.timestamp() / 86400)
        
        message = (
            f"*Hello {user.first_name}!*\n\n"
            f"*Today is:*\n"
            f"*• Persian Date:* {persian_date}\n"
            f"*• Imperial Iranian Date:* {imperial_date}\n"
            f"*• Gregorian Date:* {gregorian_date}\n\n"
            f"*Current Time:*\n"
            f"*• Tehran Time (UTC+3:30):* {tehran_time}\n"
            f"*• Universal Time (UTC):* {utc_time}\n\n"
            f"*{epoch_days} days* have passed since Unix Epoch Time"
        )
        
        await update.message.reply_text(message, parse_mode='Markdown')
    except Exception as e:
        print(f"Error: {e}")

def main():
    token = os.getenv("BOT_TOKEN")
    
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot polling run ...")
    app.run_polling()

if __name__ == "__main__":
    main()