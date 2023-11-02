import pyautogui
import pygetwindow as gw
import time

from datetime import datetime 
from datetime import timedelta 

Begindatestring = "2022-09-24"

def fillDate(xxx):
    time.sleep(2)
    Begindatestring1=xxx
    allDate=[21,34.75,34.75,29,34.5,35.25,34.75,34.25,35.75,35.5,34.5,13.25,27.25,31.25,26,33.25,33.75,32.5,34.5,35,36.75,31.25,35.5,33.25,34,33.5,34.5,25.75,29.25,35.25,33.25,33.75,34.25,33.25,33,34,33.5,33.25,34,33.75,32.75,27.5,33.5,30.5,32.75,32.5,32.75,32,31,33.25,26.5,31.5,32.25,35,33,34.5,33.5,33.5,32.5,33.75,33.25,26.75,31.25,32.75]
    for i in range(10):
        Begindate = datetime.strptime(Begindatestring1, "%Y-%m-%d")
        pyautogui.write(str(Begindate)[0:10])
        Enddate = Begindate + timedelta(days=6)
        pyautogui.write(" to ")
        pyautogui.write(str(Enddate)[0:10])
        pyautogui.press('tab')
        pyautogui.write("")
        Begindate = Enddate + timedelta(days=1)
        Begindatestring1=str(Begindate)[0:10]
        pyautogui.press('tab')

def speak():
    text = "xxxxxx Ltd."
    time.sleep(2)

    for i in range(64):
        
        pyautogui.write('15')
        time.sleep(0.1)
        for j in range(3):
            pyautogui.press('tab')
            time.sleep(0.01)
        pyautogui.write(text)
        time.sleep(0.01)
        for k in range(5):
            pyautogui.press('tab')
            time.sleep(0.01)

def concat():
    time.sleep(2)
    oddWks=[21,34.75,34.5,34.75,35.75,34.5,27.25,26,33.75,34.5,36.75,35.5,34,34.5,29.25,33.25,34.25,33,33.5,34,32.75,33.5,32.75,32.75,31,26.5,32.25,33,33.5,32.5,33.25,31.25]
    evenWks=[34.75,29,35.25,34.25,35.5,13.25,31.25,33.25,32.5,35,31.25,33.25,33.5,25.75,35.25,33.75,33.25,34,33.25,33.75,27.5,30.5,32.5,32,33.25,31.5,35,34.5,33.5,33.75,26.75,32.75]
    for i in range(32):
        pyautogui.write(str(oddWks[i]))
        pyautogui.write(",")
        pyautogui.write(str(evenWks[i]))
        pyautogui.write(",")
            
# concat();
fillDate(Begindatestring)