import os
import random
import time

import pyautogui as auto
import pywintypes
import win32gui

import clip

FLAMING_COUNT = 15
FLAMING_MESSAGES = [
    "*小丑竟是我自己",
    "*好吧，我是小丑"
]
WHEEL_CLICKS_PER_PERSON = -45


def re_login():
    os.system('taskkill /f /im QQ.exe')
    time.sleep(1.0)

    os.system('"C:\\Program Files (x86)\\Tencent\\QQ\\Bin\\QQScLauncher.exe"')
    time.sleep(1.0)

    while True:
        try:
            qq_rect()
            fail = False
        except pywintypes.error:
            fail = True
        time.sleep(1.0)
        if not fail:
            break

    auto.click(960, 650)
    while not qq_rect()[3] > 540:
        time.sleep(1.0)
    time.sleep(3.0)


def flame():
    x, y, w, h = qq_rect()
    auto.PAUSE = 1.0

    # Move cursor to the top of the QQ window
    auto.moveTo(x + 25, 0)
    auto.moveRel(0, 25)

    # Drag the QQ window out of the border of screen
    auto.click()
    auto.dragRel(0, 25, duration=1.0)
    auto.click()
    auto.dragRel(0, 25, duration=1.0)

    x, y, w, h = qq_rect()

    # Move cursor to the first person's avatar
    auto.moveTo(x + 40, y + 220)

    # Scroll to the last person's avatar
    auto.scroll(10000)  # Always start at the first person
    for i in range(FLAMING_COUNT - 1):
        auto.scroll(WHEEL_CLICKS_PER_PERSON)

    for i in range(FLAMING_COUNT):
        clip.copy(random.choice(FLAMING_MESSAGES))
        auto.doubleClick()
        time.sleep(1.0)
        auto.hotkey('ctrl', 'v')
        auto.hotkey('enter')
        time.sleep(2.0)
    auto.hotkey('alt', 'f4')

    # Reset the person list
    auto.scroll(10000)

    # Move cursor to the top of the QQ window
    auto.moveTo(x + 25, y + 20)

    # Drag the QQ window to the border of screen
    auto.dragRel(0, -100, duration=0.5)

    # Move the cursor to the center of screen
    auto.moveTo(1920 / 2, 1080 / 2)


def qq_rect():
    hwnd = win32gui.FindWindow(None, 'QQ')
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    return x, y, w, h
