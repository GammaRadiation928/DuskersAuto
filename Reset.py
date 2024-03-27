from keyboard import *
from pyautogui import *
from time import *

sleep(5)

press_and_release("o")

while locateOnScreen("Options.png", confidence=0.99) is None:
    sleep(0.01)
press_and_release("c")

while locateOnScreen("Clear.png", confidence=0.99) is None:
    sleep(0.01)
press_and_release("y")

while locateOnScreen("Options.png", confidence=0.99) is None:
    sleep(0.01)
press_and_release("b")
