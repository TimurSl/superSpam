# -*- coding: utf-8 -*-
import codecs
import sys
import time
from pathlib import Path

import keyboard
import keyboard as key
import yaml

from art import *

msg = "Spam"
interval = 0
spam_button = "f5"
is_running = False
enable_on_off = False


def invert_on_off():
    if enable_on_off:
        global is_running
        is_running = not is_running
        print("Spam is " + ("on" if is_running else "off"))


def send_msg(msg):
    key.write(msg)
    key.press_and_release("enter")
    time.sleep(interval)


def send_spam():
    invert_on_off()
    while is_running:
        send_msg(msg)


def recreate_config():
    f = open("config.yaml", "w+")
    f.write(
        "interval: 0\n"
        "spam-msg: 'Youre bad-ass!'\n"
        "spam-button: f5\n"
        "enable-on-off: false\n"
    )
    f.close()
    print("Program closes in 5 seconds")
    time.sleep(5)
    sys.exit()


def main():
    global msg
    global interval
    global spam_button
    global is_running
    global enable_on_off

    if Path("config.yaml").is_file():
        with codecs.open('config.yaml', encoding="UTF-8") as f:
            config = yaml.safe_load(f)

            try:
                msg = config["spam-msg"]
                interval = config["interval"]
                spam_button = str(config["spam-button"])
                enable_on_off = config["enable-on-off"]
            except:
                print("Error loading config file")
                recreate_config()
                sys.exit(1)


    else:
        print("Not found config file, creating...")
        recreate_config()


    """
    Напечатать в консоль текст с помощью библиотеки art
    """
    print(text2art("Spam Bot", font="small"))

    print(
        "\nCurrent settings: \n" +
        "   Interval: " + str(interval) + "\n"
        "   Message: " + msg + "\n"
        "   Button: " + spam_button + "\n"
        "   Enable on/off: " + str(enable_on_off) + "\n"
    )

    if enable_on_off:
        """
        Почему-то не работает. При нажатии на кнопку, программа ничего не делает. Поэтому пришлось сделать так: 
        """
        keyboard.add_hotkey(spam_button, lambda: send_spam(), suppress=True)

    else:
        key.add_hotkey(spam_button, lambda: send_msg(msg), suppress=True)


if __name__ == '__main__':
    main()
    keyboard.wait()
