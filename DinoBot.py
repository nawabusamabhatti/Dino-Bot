import pyautogui
import time
import keyboard
import win32api, win32con
import serial
arduino = serial.Serial(port='COM13', baudrate=9600, timeout=0.001)
Trigger = 650
SynsDelay = 1
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(Trigger, 750)[0] != 247\
            or  pyautogui.pixel(Trigger, 744)[0] != 247 \
            or pyautogui.pixel(Trigger, 730)[0] != 247 \
            or pyautogui.pixel(Trigger, 720)[0] != 247:
        # print("Pressed")
        keyboard.press('space')
        # arduino.write(bytes('1', 'utf-8'))
        time.sleep(SynsDelay/1000)
    elif pyautogui.pixel(Trigger,886)[0] != 247:
        # print("Pressed")
        keyboard.press('down')
        # arduino.write(bytes('2', 'utf-8'))
        time.sleep(SynsDelay/1000)
    print(pyautogui.pixel(Trigger, 750)[0] )









