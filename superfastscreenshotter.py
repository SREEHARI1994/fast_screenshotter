import pyautogui
import keyboard
import time
import tkinter as tk
from PIL import ImageGrab
from tkinter.filedialog import asksaveasfilename,askdirectory
app = tk.Tk()

app.attributes('-topmost', True)
n=asksaveasfilename()
name=n[n.rindex('/'):]
savelocation = askdirectory()
count=1
stop=0

while True:
    
    start=time.time()
    imagename= name + str(count) + '.jpg'
    imagepath= savelocation+imagename

    if keyboard.is_pressed('\'') and ((start-stop)>1):
        n=asksaveasfilename()
        name=n[n.rindex('/'):]
        savelocation=askdirectory()
        count=1
    
    #Full Screen
    if keyboard.is_pressed(',') and ((start-stop)>1):
        im = pyautogui.screenshot()
        im.save (imagepath)
        count=count+1
        stop=time.time()
    
    #For Instagram Stories
    elif keyboard.is_pressed('.') and ((start-stop)>1):
        im = ImageGrab.grab(bbox=(674,138,1173,983))
        im.save (imagepath)
        count=count+1
        stop=time.time()

    #For Facebook Stories
    elif keyboard.is_pressed('/') and ((start-stop)>1):
        im = ImageGrab.grab(bbox=(944,141,1419,912))
        im.save (imagepath)
        count=count+1
        stop=time.time()
         
        
        
    
