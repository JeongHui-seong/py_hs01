from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import gemini

TELEGRAM_TOKEN = ""

TRIGGER_WORDS = {
    ".":"내 성질 까먹었지"
}

async def start(update: Update, context: CallbackContext): 
    await update.message.reply_text("틀 ...")

async def monitor_chat(update: Update, context: CallbackContext):
    user_text = update.message.text
    chat_id = update.message.chat_id

    if "할머니" in user_text:
        res = gemini.genaiai(user_text.replace("할머니 ",""))
        await context.bot.send_message(chat_id=chat_id, text=res)
    else:
        for key, res in TRIGGER_WORDS.items():
            if key in user_text:
                if key == "안녕":
                    await context.bot.send_photo(chat_id=chat_id, photo=res)
                else:
                    await context.bot.send_message(chat_id=chat_id, text=res)
                break

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    #명령어 핸들러
    app.add_handler(CommandHandler("start", start))

    #응답 핸들러
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitor_chat))
    
    print("틀 ...")
    app.run_polling()

if __name__ == "__main__":
    main()
