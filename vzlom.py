import asyncio
import ctypes

import time
from pygame import mixer
import logging
import pickle
import winsound
import requests

try:
    with open('Edge_files/filename.pickle', 'rb') as pk:
        a = pickle.load(pk)
        n = a[0]
        BOT_TOKEN = a[1]
        canF = a[2]
except:
    with open('Edge_files/filename.pickle', 'wb') as pk:
        pickle.dump([0, '0', True], pk)
    n = 0
    BOT_TOKEN = '0'
    canF = True

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def g():
    global n, BOT_TOKEN, canF
    while True:
        with open('Edge_files/filename.pickle', 'rb') as pk:
            a = pickle.load(pk)
            n = a[0]
            BOT_TOKEN = a[1]
            canF = a[2]
        if canF:
            try:
                response = requests.get("https://12447695.pythonanywhere.com/api/users/" + BOT_TOKEN).json()
                n = response['IsUse']
            except Exception:
                pass
        await asyncio.sleep(5)


async def f():
    while True:
        if n == 1:
            mixer.init()
            mixer.music.load('Edge_files/agogo-bells__025_mezzo-forte_struck-singly.mp3')
            mixer.music.play()
            while mixer.music.get_busy():  # wait for music to finish playing
                time.sleep(1)
        elif n == 2:
            mixer.init()
            mixer.music.load('Edge_files/pukane-4.mp3')
            mixer.music.play()
            while mixer.music.get_busy():  # wait for music to finish playing
                time.sleep(1)
            await asyncio.sleep(1)
        elif n == 3:
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        elif n == 4:
            winsound.Beep(2500, 10000)
        elif n == 5:
            ctypes.windll.user32.MessageBoxW(0, u"Banned", u"Error", 5)
        elif n == 6:
            ctypes.windll.user32.MessageBoxW(0, u"Banned", u"Error", 5)
            winsound.Beep(2500, 10000)

        await asyncio.sleep(0.1)


async def interviews():
    tasks = [
        asyncio.create_task(f()), asyncio.create_task(g())
    ]
    await asyncio.gather(*tasks)


asyncio.run(interviews())
