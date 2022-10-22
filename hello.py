'''3 450
4 30
4 0
0 30
5 0
5 250
5 0
5 250
0 500
4 0'''
import time
from servokit import ServoKit
from playsound import playsound  
def intro():
    kit = ServoKit()
    kit.angle(7, 350)
    time.sleep(.5)
    kit.angle(7, 230)
    time.sleep(.5)
    kit.angle(3, 0)
    time.sleep(.5)
    kit.angle(3, 450)
    playsound('/media/robo/nvidia/Robo_3.0/hello.mp3', True)
    time.sleep(.5)
    kit.angle(4, 30)
    time.sleep(.5)
    kit.angle(4, 30)
    time.sleep(.5)
    kit.angle(0, 30)
    time.sleep(.5)
    kit.angle(5, 0)
    playsound('/media/robo/nvidia/Robo_3.0/i_am.mp3', True)
    time.sleep(.5)
    kit.angle(5, 270)
    time.sleep(.5)
    kit.angle(5,0)
    time.sleep(.5)
    kit.angle(5,270)
    time.sleep(.5)
    kit.angle(0,500)
    time.sleep(.5)
    kit.angle(3, 0)
    playsound('/media/robo/nvidia/Robo_3.0/into.mp3', True)

if __name__ == "__main__":
    intro()



