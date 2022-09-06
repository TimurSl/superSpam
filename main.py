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
# is_running: bool = False

# def start_spam():
#     while True:
#         if is_running:
#             send_msg(msg)

def send_msg(msg):
    key.write(msg)
    key.press_and_release("enter")
    time.sleep(interval)

# def switch_is_run():
#     global is_running
#
#     if is_running == True:
#         is_running = False
#         print(is_running)
#     else:
#         is_running = True
#         start_spam()

def main():
    global msg
    global interval
    global spam_button

    # keyboard.add_hotkey("alt+s", exit())
    if Path("config.yaml").is_file():
        with codecs.open('config.yaml') as f:
            config = yaml.safe_load(f)

            msg = config["spam-msg"]
            interval = config["interval"]
            spam_button = config["spam-button"]
            # if config["enable-switcher"] == False:
            key.add_hotkey(spam_button, lambda: send_msg(msg))
            #     print("Switcher disabled!")
            # else:
            #     key.add_hotkey(spam_button, lambda: switch_is_run())
            #     print("Switched enabled!")
    else:
        print("Not found config file, creating...")
        f = open("config.yaml", "w+")
        f.write(
            "interval: 0\n"
            "spam-msg: 'Youre bad-ass!'\n"
            "spam-button: f5\n"
            # "enable-switcher: False"
        )
        f.close()
        print("Program closes in 5 seconds")
        time.sleep(5)
        sys.exit()


    # pprint(config['enable-on-off'])
    print(
        "Super Spammer\n" +
        "\nCurrent settings: \n" +
        "Interval: " + str(interval) + "\n"
        "Message: " + msg + "\n"
        "Button: " + spam_button + "\n"
        # "Enable switcher: " + str(config["enable-switcher"]) + "\n"

    )

    while True:
        if key.read_key() == "o":
            print("App closed")
            exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()



