import pyautogui
import ctypes
import time

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
while True:
    time.sleep(1)
    dolu = pyautogui.locateOnScreen('img/dolu.png', confidence = 0.7)
    if dolu:
        print("envanter dolu")
        balikcilikscancode()
        time.sleep(1)
        PressKey(0x1C)
        ReleaseKey(0x1C)
        time.sleep(1)
        PressKey(0x1C)
        ReleaseKey(0x1C)
        time.sleep(2)
        clearchat()
