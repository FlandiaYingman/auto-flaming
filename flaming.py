import random
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

import psutil
import pyautogui as auto
import pyperclip
import pywintypes
import win32gui

# 续火联系人数量
FLAMING_COUNT = 9
# 续火消息，将在列表中随机抽取
FLAMING_MESSAGES = [
    "早上好",
    "晚上好",
]

# 滚轮滑过一名联系人所需要的 click 数，通常不需要更改
WHEEL_CLICKS_PER_PERSON = -45

# 64位系统使用
QQ_HOME = Path(r"C:\Program Files (x86)\Tencent\QQ\Bin")
# # 32位系统使用
# QQ_HOME = Path(r"C:\Program Files\Tencent\QQ\Bin")


@dataclass
class WindowRect:
    x: int
    y: int
    width: int
    height: int


def launch_qq():
    subprocess.Popen("C:\\Program Files (x86)\\Tencent\\QQ\\Bin\\QQ.exe")


def stop_qq():
    qq_procs = [proc for proc in psutil.process_iter() if proc.name() == 'QQ.exe']
    for qq_proc in qq_procs:
        qq_proc.kill()


def login():
    wait_for_login_window()
    rect = qq_rect()
    auto.click(rect.x + (rect.width / 2), rect.y + 345)
    wait_for_main_window()
    time.sleep(3.0)


def wait_for_main_window():
    max_login_window_height = 470
    min_main_window_height = 600
    while not qq_rect().height > (max_login_window_height + min_main_window_height) / 2:
        time.sleep(1.0)


def wait_for_login_window():
    while True:
        try:
            qq_rect()
            time.sleep(1.0)
            break
        except pywintypes.error:
            pass


def flame():
    auto.PAUSE = 1.0
    rect = qq_rect()

    # Drag the QQ window out of the border of screen
    while rect.y < 0:
        auto.moveTo(rect.x + 15, rect.y)
        rect = qq_rect()
        auto.moveTo(rect.x + 15, rect.y + 15)
        auto.doubleClick()
        auto.dragRel(0, 30, duration=0.25)
        rect = qq_rect()

    # Move cursor to the first person's avatar
    auto.moveTo(rect.x + 40, rect.y + 220)

    # Scroll to the last person's avatar
    auto.scroll(10000)  # Always start at the first person
    for i in range(FLAMING_COUNT - 1):
        auto.scroll(WHEEL_CLICKS_PER_PERSON)

    # Flame
    for i in range(FLAMING_COUNT):
        pyperclip.copy(random.choice(FLAMING_MESSAGES))
        auto.doubleClick()
        time.sleep(1.0)
        auto.hotkey('ctrl', 'v')
        auto.hotkey('enter')
        time.sleep(2.0)
    auto.hotkey('alt', 'f4')


def qq_hwnd():
    hwnd = win32gui.FindWindow(None, 'QQ')
    return hwnd


def qq_rect():
    hwnd = qq_hwnd()
    rect = win32gui.GetWindowRect(hwnd)
    return WindowRect(rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1])


if __name__ == '__main__':
    stop_qq()

    launch_qq()
    login()
    flame()
    stop_qq()
