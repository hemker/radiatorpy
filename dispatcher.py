import functools
from formatter import MarkdownFormatter as MF
from radiator_control import RadiatorControl

available_commands = []

def command(description):
    def command_decorator(func):
        available_commands.append('/' + func.__name__ + ' \- ' + description)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
        return wrapper
    return command_decorator


class Dispatcher:

    def __init__(self, config):
        self.control = RadiatorControl(config.rooms)
        self.available_commands = available_commands

    @command('show help')
    def help(self, update, context):
        answer = MF.list_with_heading('Available commands', self.available_commands, False)
        update.message.reply_text(answer, parse_mode='MarkdownV2', quote=False)
        
    @command('show available radiators')
    def radiators(self, update, context):
        answer = MF.list_with_heading('Available radiators', self.control.get_radiators())
        update.message.reply_text(answer, parse_mode='MarkdownV2', quote=False)

    @command('show available rooms')
    def rooms(self, update, context):
        answer = MF.list_with_heading('Available rooms', self.control.get_rooms())
        update.message.reply_text(answer, parse_mode='MarkdownV2', quote=False)

    @command('mode off')
    def off(self, update, context):
        answer = {}
        for radiator in self.__parse_radiator(context.args):
            answer[radiator] = self.control.mode_off(radiator)
        
        update.message.reply_text(MF.map_with_heading('New mode\(s\)', answer), parse_mode='MarkdownV2', quote=False)

    @command('mode auto')
    def auto(self, update, context):
        answer = {}
        for radiator in self.__parse_radiator(context.args):
            answer[radiator] = self.control.mode_auto(radiator)
        
        update.message.reply_text(MF.map_with_heading('New mode\(s\)', answer), parse_mode='MarkdownV2', quote=False)

    @command('mode manual')
    def manual(self, update, context):
        answer = {}
        for radiator, temperature in self.__parse_radiator(context.args):
            answer[radiator] = self.control.mode_manual(radiator, temperature)
        
        update.message.reply_text(MF.map_with_heading('New mode\(s\)', answer), parse_mode='MarkdownV2', quote=False)

    def __parse_radiator(self, args):
        if not args:
            return self.control.get_radiators()
        elif len(args) == 1:
            try:
                temperature = float(args[0])
                return [(radiator, temperature) for radiator in self.control.get_radiators()]
            except ValueError:
                return [args[0]]
        else:
            return [(args[0], float(args[1]))]

    @command('request status')
    def status(self, update, context):
        answer = {}
        for radiator in self.__parse_radiator(context.args):
            answer[radiator] = self.control.get_status(radiator)

        update.message.reply_text(MF.map_with_heading('Status', answer), parse_mode='MarkdownV2', quote=False)