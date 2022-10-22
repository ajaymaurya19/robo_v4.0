# Import Required Library
import datetime
from tkinter import *
from datetime import datetime

import time
#import winsound
from threading import *


def Threading(alarms):
	t1=Thread(target=alarm, args=(alarms,))
	t1.start()

def alarm(alarm_time):
	# Infinite Loop


    alarm_hour = alarm_time[0:2]
    alarm_min = alarm_time[3:5]
    alarm_sec = 00
    alarm_period = alarm_time[9:].upper()

    while True:
        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_sec = now.strftime("%S")
        current_period = now.strftime("%p")

        if alarm_period == current_period:
            if alarm_hour == current_hour:
                if alarm_min == current_min:
                    if alarm_sec == current_sec:
                        print("Wake Up!")
                        #playsound('D:/Library/Documents/Projects/Coding/Beginner Python Projects/Alarm Clock/alarm.wav')
                        break
    
def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            f = open('/media/robo/nvidia/Robo_3.0/alarms.txt', "a")
            f.write(f'\n{alarm_time}')
            f.close()

            return "ok"
        
while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
    
    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        
        
        Threading(alarm_time)

