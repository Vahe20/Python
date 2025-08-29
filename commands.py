import webbrowser
import os
import requests
import random
import datetime
import pyautogui
import time
import threading
import re
from plyer import notification

import config
import Timer


def openYoutube():
    webbrowser.open("https://www.youtube.com/")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openYandex():
    webbrowser.open("https://yandex.ru/")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openSteam():
    os.startfile(config.steam)
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openVscode():
    os.startfile(config.vsCode)
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openDiscord():
    os.startfile(config.discord)
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def openEpicGames():
    os.startfile(config.epicGames)
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def gtaRp():
    os.startfile(config.gtaRp)
    return openEpicGames()

def weather():
    url = "http://wttr.in/Yerevan?format=%t"
    weather = requests.get(url)
    return weather.text

def time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def screenShot():
    screenshot = pyautogui.screenshot()
    screenshot.save(config.dirPath + "/screenshots/screenshot.png")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])

def jarvis_timer(command):
    match = re.search(r'(\d+)\s*(минут|мин|секунд|сек)', command.lower())
    if not match:
        print("Не удалось распознать время!")
        return

    number = int(match.group(1))
    unit = match.group(2)

    seconds = number * 60 if 'мин' in unit else number

    name_match = re.search(r'для (.+)', command.lower())
    name = name_match.group(1).capitalize() if name_match else "Таймер"

    message = f"Таймер '{name}' завершен!"

    timer = Timer.Timer(name, seconds, message)
    timer.start()


def powerOff():
    os.system("shutdown /s /t 1")
    return random.choice(["Загружаю сэр", "Всегда к вашим услугам сэр", "Запрос выполнен сэр", "К вашим услугам сэр"])
    

def executor(funcName):

    return globals()[funcName]()
