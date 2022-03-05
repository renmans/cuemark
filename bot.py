import youtube_dl
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

token = ''


def ping(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Pong")


'''
def test(update: Update, context: CallbackContext) -> None:
    # video
    # update.message.reply_video(open('test.gif', 'rb'))
    # gif
    # update.message.reply_animation(open('test.gif', 'rb'))
    # audio
    # update.message.reply_audio(open('test.gif', 'rb'))
    pass
'''


class Cuemark:
    def __init__(self):
        # url = self.url
        # _type = self._type
        pass

    def get_video(self):
        pass

    def get_audio(self):
        pass

    def get_preview(self):
        pass

    def reply(self, file):
        pass

    def error_message(self):
        pass

    @staticmethod
    def crop_frame():
        pass

    @staticmethod
    def convert_to_gif():
        pass

    def test(self, update, context):
        update.message.reply_text("Class")


cuemark = Cuemark()

updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler('ping', ping))
updater.dispatcher.add_handler(CommandHandler('test', cuemark.test))


updater.start_polling()
updater.idle()
