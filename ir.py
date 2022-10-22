import threading
from RPi import GPIO
from time import sleep

left_ir = 36
right_ir= 35

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(left_ir, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(right_ir, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
'''
counter = 0
d0LastState = False

try:
        while True:
                currentState = GPIO.input(d0)
                #print (counter)
                if currentState != d0LastState:
                        counter +=1
                        print (counter)
                d0LastState = currentState

finally:
        GPIO.cleanup()'''
value = None

def Left_ir():
    counterl = 0
    print ('WorkerA start')
    d0LastState = False
    while True:
                currentState = GPIO.input(left_ir)
                print (f'Left {counterl}')
                if currentState != d0LastState:
                        counterl +=1
                        print (f'Left {counterl}')
                d0LastState = currentState

def Right_ir():
    counterr = 0
    d0LastStater = False
    print ('WorkerB start')
    while True:
                currentStater = GPIO.input(right_ir)
                #print (f'Right {counterr}')
                if currentStater != d0LastStater:
                        counterr +=1
                        print (f'Right {counterr}')
                d0LastStater = currentStater

'''ta = threading.Thread(target=Left_ir)
ta.start()

tb = threading.Thread(target=Right_ir)
tb.start()'''
Left_ir()
