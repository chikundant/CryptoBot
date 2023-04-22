from project import bot, app
import config
import flask
import telebot
from datetime import datetime
import os
from project.models import Base
from project import engine

last_update_time = datetime.now()

if app.debug is True:
    bot.remove_webhook()
    Base.metadata.create_all(engine)
    bot.infinity_polling()
else:
    @app.route('/' + config.BOT_API, methods=['POST'])
    def get_message():
        global last_update_time
        if flask.request.headers.get('content-type') == 'application/json':
            json_string = flask.request.get_data().decode('utf-8')
            update = telebot.types.Update.de_json(json_string)
            print('[GOT UPDATES]')
            try:
                if update.message.date is not None:
                    update_time = datetime.fromtimestamp(update.message.date)

                    if update_time > last_update_time:
                        bot.process_new_updates([update])
                    return '!', 200
            except Exception as e:
                print(f'[EXCEPTION {e} - MESSAGE:{update.message}]')

            return '!', 200
        else:
            flask.abort(403)


    @app.route('/')
    def webhook():
        bot.delete_webhook()
        bot.set_webhook(url=config.WEB_HOOK_URL)
        return '!', 200


    if __name__ == '__main__':

        app.run(host=config.APP_HOST, port=int(os.environ.get('PORT', 5000)))
