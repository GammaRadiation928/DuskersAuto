from keyboard import *
from pyautogui import *
from time import *

sleep(5)
press_and_release("p")

while locateOnScreen("Training.png", confidence=0.99) is None:
    sleep(0.01)
press_and_release("n")

while locateOnScreen("YorN.png", confidence=0.99) is None:
    press_and_release("enter")
    sleep(0.01)
press_and_release("n")
