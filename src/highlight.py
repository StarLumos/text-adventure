from typing import Any
from sty import fg, Style, RgbFg

def red(message: str | Any) -> str:
    return fg.red + str(message) + fg.white

def yellow(message: str | Any) -> str:
    return fg.yellow + str(message) + fg.white

def green(message: str | Any) -> str:
    return fg.green + str(message) + fg.white

def blue(name: str | Any) -> str:
    return fg.blue + str(name) + fg.white

def cyan(name: str | Any) -> str:
    return fg.cyan + str(name) + fg.white

def magenta(name: str | Any) -> str:
    return fg.magenta + str(name) + fg.white

def white(name: str | Any) -> str:
    return fg.white + str(name) + fg.white

def black(name: str | Any) -> str:
    return fg.black + str(name) + fg.white
