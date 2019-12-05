from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('Hello we started!')

def echo(update, context):
    update.message.reply_text(update.message.text)

if __name__ == '__main__':
    TOKEN = '932851484:AAE1KUFSPAahJrPgtw91XksyJYnvYPcC3Ns'

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()
