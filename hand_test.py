from servokit import ServoKit
import time
kit = ServoKit()
kit.angle(3, 0)
kit.angle(3, 470)
for i in range (0,2):
    kit.angle(4, 0)
    time.sleep(1)
    kit.angle(4, 40)
    time.sleep(1)
kit.angle(3, 0)