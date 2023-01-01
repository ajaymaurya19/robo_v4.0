
from datetime import datetime

from threading import *


def Threading(alarms):
	t1=Thread(target=alarm, args=(alarms,message))
	t1.start()

def alarm(alarm_time):
    alarm_hour = alarm_time[0:2]
    alarm_min = alarm_time[3:5]
    alarm_period = alarm_time[9:].upper()

    while True:
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        #current_sec = now.strftime("%S")
        current_period = now.strftime("%p")

        if alarm_period == current_period:
            if alarm_hour == current_hour:
                if alarm_min == current_min:
                    
                    print("Wake Up!")
                    #playsound('D:/Library/Documents/Projects/Coding/Beginner Python Projects/Alarm Clock/alarm.wav')
                    break
    
def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        else:
            f = open('alarms.txt', "a")
            f.write(f'\n{alarm_time}')
            f.close()

            return "ok"
        
while True:
    command = input("Enter...")
    if "robo set alarm" in command:
        alarm_time = input("Enter time in 'HH:MM AM/PM' format: ")
        #after  one hour
        if "hour" in command:
            command.replace('hour')
            if "after" in command:
                command.replace('after')
            elif 'one' in command:
                print("setting alarm after one Hour")
            elif 'two' in command:
                print("setting alarm after two Hour")
            elif 'three' in command:
                print("setting alarm after three Hour")     
            elif 'four' in command:
                print("setting alarm after four Hour")
            elif 'five' in command:
                print("setting alarm after five Hour")
            elif 'six' in command:
                print("setting alarm after six Hour")
            elif 'seven' in command:
                print("setting alarm after seven Hour")     
            elif 'eight' in command:
                print("setting alarm after eight Hour")
            elif 'nine' in command:
                print("setting alarm after nine Hour")
            elif 'ten' in command:
                print("setting alarm after ten Hour")
            elif 'eleven' in command:
                print("setting alarm after eleven Hour")     
            elif 'twelve' in command:
                print("setting alarm after twelve Hour")
        if "minute" in command:
            command.replace('hour')
            if "after" in command:
                command.replace('after')

if "one"in command:
    print("setting alarm after one")
elif 'two' in command:
    print("setting alarm after")
elif 'three' in command:
    print("setting alarm after")
elif 'four' in command:
    print("setting alarm after")
elif 'five' in command:
    print("setting alarm after")
elif 'six' in command:
    print("setting alarm after")
elif 'seven' in command:
    print("setting alarm after")
elif'eight' in command:
    print("setting alarm after")
elif 'nine' in command:
    print("setting alarm after")
elif 'ten' in command:
    print("setting alarm after")
elif 'eleven' in command:
    print("setting alarm after")
elif 'twelve' in command:
    print("setting alarm after")
elif 'thirteen' in command:
    print("setting alarm after")
elif 'fourteen' in command:
    print("setting alarm after")
elif 'fifteen' in command:
    print("setting alarm after")
elif 'sixteen' in command:
    print("setting alarm after")
elif 'seventeen' in command:
    print("setting alarm after")
elif 'eighteen' in command:
    print("setting alarm after")
elif 'nineteen' in command:
    print("setting alarm after")
elif 'twenty' in command:
    print("setting alarm after")
elif 'twenty-one' in command:
    print("setting alarm after")
elif 'twenty-two' in command:
    print("setting alarm after")
elif 'twenty-three' in command:
    print("setting alarm after")
elif 'twenty-four' in command:
    print("setting alarm after")
elif 'twenty-five' in command:
    print("setting alarm after")
elif 'twenty-six' in command:
    print("setting alarm after")
elif 'twenty-seven' in command:
    print("setting alarm after")
elif 'twenty-eight' in command:
    print("setting alarm after")
elif 'twenty-nine' in command:
    print("setting alarm after")
elif 'thirty' in command:
    print("setting alarm after")
elif 'thirty-one' in command:
    print("setting alarm after")
elif 'thirty-two' in command:
    print("setting alarm after")
elif 'thirty-three' in command:
    print("setting alarm after")
elif 'thirty-four' in command:
    print("setting alarm after")
elif 'thirty-five' in command:
    print("setting alarm after")
elif 'thirty-six' in command:
    print("setting alarm after")
elif 'thirty-seven' in command:
    print("setting alarm after")
elif 'thirty-eight' in command:
    print("setting alarm after")
elif 'thirty-nine' in command:
    print("setting alarm after")
elif 'forty' in command:
    print("setting alarm after")
elif 'forty-one' in command:
    print("setting alarm after")
elif 'forty-two' in command:
    print("setting alarm after")
elif 'forty-three' in command:
    print("setting alarm after")
elif 'forty-four' in command:
    print("setting alarm after")
elif 'forty-five' in command:
    print("setting alarm after")
elif 'forty-six' in command:
    print("setting alarm after")
elif 'forty-seven' in command:
    print("setting alarm after")
elif 'forty-eight' in command:
    print("setting alarm after")
elif 'forty-nine' in command:
    print("setting alarm after")
elif 'fifty' in command:
    print("setting alarm after")
elif 'fifty-one' in command:
    print("setting alarm after")
elif 'fifty-two' in command:
    print("setting alarm after")
elif 'fifty-three' in command:
    print("setting alarm after")
elif 'fifty-four' in command:
    print("setting alarm after")
elif 'fifty-five' in command:
    print("setting alarm after")
elif 'fifty-six' in command:
    print("setting alarm after")
elif 'fifty-seven' in command:
    print("setting alarm after")
elif 'fifty-eight' in command:
    print("setting alarm after")
elif 'fifty-nine'in command:
    print("setting alarm after")
elif 'sixty' in command:
    print("setting alarm after")
                
            
            
            
            
            
        
        validate = validate_time(alarm_time.lower())
        if validate != "ok":
            print(validate)
        else:
            print(f"Setting alarm for {alarm_time}...")
            Threading(alarm_time)



