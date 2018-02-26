import ctypes
import win32api
import time
import random
#from pynput.mouse import Listener

#Create a function that takes the number of clicks as a prameter
#end = False

#def onScroll(x, y, dx, dy):
#        end = True
#        return False

def get_position():
    """get mouse position"""
    return win32api.GetCursorPos()

def click(point = None):
    pos = list(get_position())
    if point is None:
        point = pos
    ctypes.windll.user32.SetCursorPos(point[0], point[1])
    pos = list(get_position())
    while pos == point:
        if (not pos==point):
            break
                
        ctypes.windll.user32.mouse_event(2,0,0,0,0)
        ctypes.windll.user32.mouse_event(4,0,0,0,0)
        sleepTime = random.uniform(.03, .028)
        time.sleep(sleepTime)

        pos = list(get_position())

click()
