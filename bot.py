import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('Hello we started!')

def echo(update, context):
    update.message.reply_text(update.message.text)

if __name__ == '__main__':
    TOKEN = '932851484:AAE1KUFSPAahJrPgtw91XksyJYnvYPcC3Ns'
    NAME = 'comm-unist-deploy'

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))

    PORT = os.environ.get('PORT')
    updater.start_webhook(listen='0.0.0.0',
                          port=int(PORT),
                          url_path=TOKEN)

    updater.bot.setWebhook('https://%s.herokuapp.com/%s' % (NAME, TOKEN))

    updater.idle()
