from keyboard import *
from pyautogui import *
from time import *

sleep(5)

press_and_release("p")  # Starts the game

while locateOnScreen("YorN.png", confidence=0.99) is None:
    sleep(0.01)
press_and_release("n")  # Skips tutorial

while locateOnScreen("Spam.png", confidence=0.99) is None:
    sleep(0.01)  # Waits until it sees a specific object on screen

while locateOnScreen("Map.png", confidence=0.99) is None:  # Until we see the map it spams enter
    press_and_release("enter")
    sleep(0.1)

if locateOnScreen("Overshot.png", confidence=0.9) is not None:
    press_and_release("esc")

print(list(locateAllOnScreen("Derelict.png", confidence=0.92)))
