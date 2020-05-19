from telegram.ext import Updater, CommandHandler
from radiator_control import RadiatorControl
from dispatcher import Dispatcher
import config

dispatcher = Dispatcher(config)
updater = Updater(config.token, use_context=True)

updater.dispatcher.add_handler(CommandHandler('radiators', dispatcher.radiators))
updater.dispatcher.add_handler(CommandHandler('rooms', dispatcher.rooms))
updater.dispatcher.add_handler(CommandHandler('help', dispatcher.help))
updater.dispatcher.add_handler(CommandHandler('off', dispatcher.off))
updater.dispatcher.add_handler(CommandHandler('auto', dispatcher.auto))
updater.dispatcher.add_handler(CommandHandler('manual', dispatcher.manual))

updater.start_polling()
updater.idle()