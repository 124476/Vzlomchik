import time
from pygame import mixer

import keyboard

for i in range(50):
    keyboard.send("volume up")

mixer.init()
mixer.music.load('Edge_files/pukane-4.mp3')
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)

for i in range(50):
    keyboard.send("volume down")
