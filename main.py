# -*- coding: utf-8 -*-
import codecs
import sys
import time
from pathlib import Path

import keyboard
import keyboard as key
import yaml

msg = "Spam"
interval = 0
spam_button = "f5"

def send_msg(msg):
    key.write(msg)
    key.press_and_release("enter")
    time.sleep(interval)

def main():
    global msg
    global interval
    global spam_button

    if Path("config.yaml").is_file():
        with codecs.open('config.yaml', encoding="UTF-8") as f:
            config = yaml.safe_load(f)

            msg = config["spam-msg"]
            interval = config["interval"]
            spam_button = str(config["spam-button"])
            key.add_hotkey(spam_button, lambda: send_msg(msg))
    else:
        print("Not found config file, creating...")
        f = open("config.yaml", "w+")
        f.write(
            "interval: 0\n"
            "spam-msg: 'Youre bad-ass!'\n"
            "spam-button: f5\n"
        )
        f.close()
        print("Program closes in 5 seconds")
        time.sleep(5)
        sys.exit()


    print(
        "Super Spammer\n" +
        "\nCurrent settings: \n" +
        "Interval: " + str(interval) + "\n"
        "Message: " + msg + "\n"
        "Button: " + spam_button + "\n"

    )

    while True:
        # dont close program
        if key.read_key() == "alt+s":
            print("App closed")
            exit()

if __name__ == '__main__':
    main()



