import os


class Colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    def clear():
        os.system('clear')

    class foreground:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class background:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


def bordered(text, border_color):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    print(border_color, '┌' + '─' * width + '┐', Colors.reset)
    [print(border_color, '│' + (s + ' ' * width)[:width] + '│', Colors.reset) for s in lines]
    print(border_color, '└' + '─' * width + '┘', Colors.reset)


def coloured_bordered(text, colour=Colors.background.cyan):
    Colors.clear()
    bordered(text, colour)
    input()
