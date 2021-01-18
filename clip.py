import pyperclip as pyperclip
import win32clipboard


def copy(content):
    if str(content).startswith("*"):
        content = str(content).removeprefix("*")
        _copy_image(content + ".dib")
    else:
        _copy_text(content)


def _copy_text(text):
    pyperclip.copy(text)


def _copy_image(file):
    with open(file, 'rb') as file:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIBV5, file.read())
        win32clipboard.CloseClipboard()


def clear():
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()


def _save_image(file):
    with open(file, 'wb') as file:
        win32clipboard.OpenClipboard()
        file.write(win32clipboard.GetClipboardData(win32clipboard.CF_DIBV5))
        win32clipboard.CloseClipboard()
