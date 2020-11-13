#   Use Case:   Monitoring message with alarm on window (Like Telegram)
#   Developer:  Nitish Gupta
#   Date:       11/05/2020

import pyscreenshot as ImageGrab
import time
from PIL import Image
import numpy as np
import cv2
import pytesseract
from pytesseract import Output
from playsound import playsound
import pyautogui, sys

times = 10

while True:
    # Keeping the window active and updated (helps to scroll down to latest msg every 10 count)
    if times == 0:
        pyautogui.click(x=310, y=280)
        times = 10
    times = times - 1

    # Grab this area of window
    im = ImageGrab.grab(bbox=(560,210,1150,1000))

    # Preparing your image (Color to BW)
    image = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY)
    image = 255 - image
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imwrite("./slot_ss.png", image)

    # Find Text in the image
    d = pytesseract.image_to_string(image).split()
    # print(d)
    
    # Msg to look for (in this example "go")
    if "Go" in d or "go" in d or "GO" in d:
        
        print("\n[+] Slots Available!!!\nWake up!")
        print(d)

        while True:
            playsound('alarm.mp3')

    # time.sleep(2)
    # print("waiting...")