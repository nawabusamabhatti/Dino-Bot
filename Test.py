# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM13', baudrate=115200, timeout=.1)
def write_read(x):

    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value