from servokit import ServoKit
kit = ServoKit()
'''kit.servo[3].angle=180
kit.servo[0].angle=180'''


#from gpiozero import Servo, DistanceSensor
from guizero import App, Box, Text, PushButton, Slider
from time import sleep

'''servo = Servo(17, 0, 0.0005, 0.0025)
sensor = DistanceSensor(echo=18, trigger=27)'''

def ServoPosition1(slider_value):
    kit.angle(0, int(slider_value))
    #servo.value = int(slider_value) / 90

def ServoPosition2(slider_value):
    kit.angle(1, int(slider_value))

def ServoPosition3(slider_value):
    kit.angle(2, int(slider_value))


def ServoPosition4(slider_value):
    kit.angle(3, int(slider_value))


def ServoPosition5(slider_value):
    kit.angle(4, int(slider_value))


def ServoPosition6(slider_value):
    kit.angle(5, int(slider_value))


def ServoPosition7(slider_value):
    kit.angle(6, int(slider_value))

def ServoPosition8(slider_value):
    kit.angle(7, int(slider_value))

def my_user_task():
    pass
    '''print("Distance: {0:.2f}cm".format(sensor.distance * 100))
    reading_text.value = "{0:.2f}".format(sensor.distance * 100)'''

app = App(title="Servo GUI", width=500, height=550, layout="auto")

instruction_text = Text(app, text="Drag slider below to control servo position.")
instruction_text.repeat(1000, my_user_task)
reading_text = Text(app, text="Servo 1 right hand")
servo_position = Slider(app, command=ServoPosition1, start=0, end=500, width='fill')
reading_text = Text(app, text="Servo 2 up down")
servo_position = Slider(app, command=ServoPosition2, start=0, end=500, width='fill')
reading_text = Text(app, text="Servo 3 left hand")
servo_position = Slider(app, command=ServoPosition3, start=0, end=500, width='fill')
reading_text = Text(app, text="Servo 4")
servo_position = Slider(app, command=ServoPosition4, start=0, end=500, width='fill')
reading_text = Text(app, text="Servo 5 up down")
servo_position = Slider(app, command=ServoPosition5, start=0, end=500, width='fill')
reading_text = Text(app, text="Servo6")
servo_position = Slider(app, command=ServoPosition6, start=0, end=500, width='fill')
reading_text = Text(app, text="Servo 7 left right")
servo_position = Slider(app, command=ServoPosition7, start=100, end=400, width='fill')
reading_text = Text(app, text="Servo 8 up dowm")
servo_position = Slider(app, command=ServoPosition8, start=150, end=400, width='fill')
#distance_text = Text(app, text="Distance (cm):")
#reading_text = Text(app, text="Servo")
#designby_text = Text(app, text="Idris - Cytron Technologies", align='bottom')

app.display()