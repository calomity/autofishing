import os
import cv2
import sys
import time
import ctypes
import numpy as np
import keyboard
import win32gui
import pyautogui
import ocrmodule
import imageprocessingmodule
import logmodule
import configmodule

print("start")

SendInput = ctypes.windll.user32.SendInput

PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def getscreenshot(path):
	png = ".png"
	if png in path:
		print("Found")
	else:
		print("Not Found")
	image = pyautogui.screenshot(region=(500, 500, 400, 250))
	image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
	cv2.imwrite(path,image)

def balikcilikscancode():
    PressKey(0x14)#t
    ReleaseKey(0x14)#t
    PressKey(0x36)#/
    PressKey(0x08)#/
    ReleaseKey(0x36)#/
    ReleaseKey(0x08)#/
    PressKey(0x30)#b
    ReleaseKey(0x30)#b
    PressKey(0x1E)#a
    ReleaseKey(0x1E)#a
    PressKey(0x26)#l
    ReleaseKey(0x26)#l
    PressKey(0x28)#i
    ReleaseKey(0x28)#i
    PressKey(0x25)#k
    ReleaseKey(0x25)#k
    PressKey(0x2E)#c
    ReleaseKey(0x2e)#c
    PressKey(0x28)#i
    ReleaseKey(0x28)#i
    PressKey(0x26)#l
    ReleaseKey(0x26)#l
    PressKey(0x28)#i
    ReleaseKey(0x28)#i
    PressKey(0x25)#k
    ReleaseKey(0x25)#k
    PressKey(0x1C)#enter
    ReleaseKey(0x1C)#enter
def clearchat():
    PressKey(0x14)#t
    ReleaseKey(0x14)#t
    PressKey(0x36)#/
    PressKey(0x08)#/
    ReleaseKey(0x36)#/
    ReleaseKey(0x08)#/
    PressKey(0x2E)#c
    ReleaseKey(0x2e)#c
    PressKey(0x2E)#c
    ReleaseKey(0x2E)#c
    PressKey(0x1C)#enter
    ReleaseKey(0x1C)#enter

def detectinventory():
    dolu = pyautogui.locateOnScreen('img/dolu.png', confidence = 0.7)
    if dolu:
    	os.system("taskkill /f /im  balikcilik.exe")
    	print("envanter dolu")
    	balikcilikscancode()
    	time.sleep(1)
    	PressKey(0x1C)
    	ReleaseKey(0x1C)	
    	for x in range(15):
        	time.sleep(0.2)
        	keyboard.press('down')
    	time.sleep(1)
    	PressKey(0x1C)
    	ReleaseKey(0x1C)
    	time.sleep(2)
    	clearchat()
    	os.system("start C:\\balikcilik\\balikcilik.exe")
    	time.sleep(1)
    	handle2 = win32gui.FindWindow(0, "GTA:SA:MP")
    	win32gui.SetForegroundWindow(handle2) 

def detectdialogbox():
	pyautogui.FAILSAFE = False
	dialogbox = pyautogui.locateOnScreen('img/boximage/dialogbox.png', confidence = 0.7)
	if dialogbox:
		os.system("taskkill /f /im balikcilik.exe")
		print("Detected")
		getscreenshot("img/screen.png")
		time.sleep(5)
		imageprocessingmodule.firstconvert("img/screen.png")
		imageprocessingmodule.secondconvert("img/first.png")
		imageprocessingmodule.lastconvert("img/second.png")
		#code = ocrmodule.tesseract('img/last.png','C:\\Program Files\\Tesseract-OCR\\tesseract.exe')
		code = ocrmodule.paddlepaddle('img/last.png','en','PP-OCRv2')
		print (code)
		box = pyautogui.locateOnScreen('img/boximage/box.png', confidence = 0.7)
		print("box araniyor")
		if box:
			print("box bulundu")
			time.sleep(1)
			PressKey(0x38)
			PressKey(0x0F)
			ReleaseKey(0x38)
			ReleaseKey(0x0F)
			time.sleep(1)
			handle = win32gui.FindWindow(0, "GTA:SA:MP")  
			win32gui.SetForegroundWindow(handle) 
			time.sleep(1)
			pyautogui.moveTo(box)
			pyautogui.click(box)
			for x in range(25):
				PressKey(0x0E)
				ReleaseKey(0x0E)
			pyautogui.write(code)
			time.sleep(0.5)
			PressKey(0x1C)
			ReleaseKey(0x1C)
			time.sleep(0.5)
			os.system("start C:\\balikcilik\\balikcilik.exe")
			time.sleep(1)
			handle1 = win32gui.FindWindow(0, "GTA:SA:MP")  
			win32gui.SetForegroundWindow(handle1) 



while True:
    detectinventory()
	detectdialogbox()