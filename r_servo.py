'''#intilized angle 
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


dis = DistanceSensor()'''
def main_roboAI2(q):
    from servokit import ServoKit
    kit = ServoKit()
    kit.angle(6, 250)
    kit.angle(7, 400)
    rightMotor = Motor(32,21,19)
    leftMotor = Motor(33,26,24)
    speed = 50
        
    leftMotor.setSpeed(speed)
    rightMotor.setSpeed(speed)
    
    
    
    while True:        
        data = dis.getDistance()
        #print(data)
        if not q.empty():
            q_is = q.get()
            if q_is =="END":
                break
            if q_is =="stop":
                break
        if data == -1:
            continue
        if data < 25:
            print('stop')
            leftMotor.stop()
            rightMotor.stop()
        if data >25:
                #print(data)
            print("goForward")
            leftMotor.goForward()
            rightMotor.goForward()
        elif data < 25: 
            print("stop")
       
            
      
            kit.angle(6, 100)
            kit.angle(7, 400)
            time.sleep(1)
            left_dis = dis.getDistance()
            
            kit.angle(6, 350)
            kit.angle(7, 400)

           
            time.sleep(1)
            right_dis = dis.getDistance()
            kit.angle(6, 250)
            kit.angle(7, 400)

            if left_dis and right_dis< 15:
                print("gobackword")
                leftMotor.goBackward()
                rightMotor.goBackward()
                time.sleep(2)
            elif left_dis > right_dis:
                print("goleft")
                leftMotor.stop()
                rightMotor.goForward()
                time.sleep(5)
            elif left_dis < right_dis:
                print('goright')
                leftMotor.goForward()
                rightMotor.stop()
                time.sleep(5)
def move_auto():
    print("Moveing in Autopilet mode")