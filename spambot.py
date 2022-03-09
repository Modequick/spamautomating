import time
import pyautogui
import os

os.chdir(r"C:/Users/kevin/OneDrive/Desktop/spambot")
time.sleep(3)

def sendspambot():
    for i in range(600):
        pyautogui.typewrite(["%","f"])
        pyautogui.press("enter")
        print("complete",i,"loops")
        check = pyautogui.locateOnScreen("captchaiconbrowser.png")
        time.sleep(1)
        if (check == None) is False : 
            print("Bot is done, with", i , "loops")
            break
        

sendspambot()




