import time
import sys

def display(message: str, delay: float = 0.05, newlines: int = 1) -> None:
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newlines > 0:
        sys.stdout.write("\n" * newlines)

def prompt(message: str = "", delimiter: str = ": ", delay: float = 0.05, newlines: int = 0) -> str:
    display(message + delimiter, delay, newlines)
    return input()
