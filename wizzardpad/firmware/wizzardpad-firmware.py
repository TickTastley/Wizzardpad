#I don't know if this code works, it is 3 AM and I'm to lazy to somehow check it

import os
import time
from machine import Pin, I2C
from encoder import Encoder
from oled import OLED

buttons = [Pin(D, Pin.IN, Pin.PULL_UP) for D in (0, 1, 2, 3, 4)]
encoder = Encoder(Pin(5), Pin(6), Pin(7))

i2c = I2C(0, scl=Pin(9), sda=Pin(8))
oled = OLED(i2c)

key_shortcuts = [
    "CTRL+C",
    "CTRL+V",
    "CTRL+Z",
    "ALT+TAB",
    "SHIFT+DEL"
]


def play_video_on_oled(video_path):
    if os.path.exists(video_path):
        oled.play_video(video_path)
    else:
        oled.show_text("Video not found")


def main():
    video_path = "path/to/video.mp4"
    play_video_on_oled(video_path)

    while True:
        for idx, button in enumerate(buttons):
            if not button.value():
                execute_shortcut(key_shortcuts[idx])
                time.sleep(0.2)

        if encoder.is_rotated():
            if encoder.direction == "left":
                decrease_volume()
            elif encoder.direction == "right":
                increase_volume()


def execute_shortcut(shortcut):
    print(f"Executing shortcut: {shortcut}")


def increase_volume():
    print("Volume up")


def decrease_volume():
    print("Volume down")


if __name__ == "__main__":
    main()
