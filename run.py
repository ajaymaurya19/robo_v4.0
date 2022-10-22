from playsound import playsound  
from servokit import ServoKit
import time
kit = ServoKit()
kit.angle(0, 500)
kit.angle(1, 500)
kit.angle(2, 250)
kit.angle(3, 40)
kit.angle(4, 15)
kit.angle(5, 290)
kit.angle(6, 240)
kit.angle(7, 200)



def greeting():
    

    playsound('/media/robo/nvidia/Robo_3.0/good.mp3', True)

    playsound('/media/robo/nvidia/Robo_3.0/college.mp3', True)
    playsound('/media/robo/nvidia/Robo_3.0/hello.mp3', True)
    playsound('/media/robo/nvidia/Robo_3.0/introd.mp3', True)

    playsound('/media/robo/nvidia/Robo_3.0/birth.mp3', True)




    kit.angle(0, 250)
    kit.angle(3, 250)
    time.sleep(10)
    kit.angle(3, 0)
    kit.angle(0, 500)

greeting()