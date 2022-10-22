from datetime import date
import RPi.GPIO as GPIO
import time

from cv2 import morphologyEx

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

class Motor:
    def __init__(self,EN, IN1, IN2):
        self.speed = EN
        
        self.forward = IN1
        self.backward = IN2
        self.pwm = None
    

        # pins setup
        GPIO.setup(self.speed, GPIO.OUT, initial=GPIO.LOW)
 
        GPIO.setup(self.forward, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.backward, GPIO.OUT, initial=GPIO.LOW)

        self.pwm = GPIO.PWM(self.speed, 50) # frequency of pwm signal: 50Hz
        self.pwm.start(0)
       

    def goForward(self):
        GPIO.output(self.forward, GPIO.HIGH)
        GPIO.output(self.backward, GPIO.LOW)

    def goBackward(self):
        GPIO.output(self.forward, GPIO.LOW)
        GPIO.output(self.backward, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.forward, GPIO.LOW)
        GPIO.output(self.backward, GPIO.LOW)
    def setSpeed(self, value):
        # value must be between 0 and 100
        # 0->min speed | 100 -> max speed
        if value < 0:
            value = 0
        elif value > 100:
            value = 100
        self.pwm.ChangeDutyCycle(value)


    

    def __del__(self):
        # cleanup and leave pins in the safe state
        self.stop()
     
        GPIO.cleanup([self.forward, self.backward])

class DistanceSensor:
    def __init__(self, TRIGGER = 15, ECHO=16):
        self.trig = TRIGGER
        self.echo = ECHO

    # This function returns distance in cm or -1 value if the measurement failed.
    # Distance measurement using a ultrasonic sensor is a time-sensitive work.
    # So, because here runs Ubuntu OS, I think it depends by process scheduling.
    # Sometimes it work with an error of max 2 cm, sometimes it doesn't.
    # Doesn't work for distance < 4 cm (echo pulse is too fast ~230us).
    def getDistance(self):
        # pins setup
        GPIO.setup(self.trig, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.echo, GPIO.IN)

        # set Trigger to HIGH for 10 us
        GPIO.output(self.trig, GPIO.HIGH)
        time.sleep(0.00001) # 10 us
        GPIO.output(self.trig, GPIO.LOW)

        # start counting time at Echo rising edge
        GPIO.wait_for_edge(self.echo, GPIO.RISING, timeout=100) # 100 ms
        startTime = time.time()

        # stop counting time at Echo falling edge
        GPIO.wait_for_edge(self.echo, GPIO.FALLING, timeout=100) # 100 ms
        elapsedTime = time.time() - startTime   # in seconds

        distance = -1
        # check if the measurement succeeded
        if elapsedTime < 0.1:
            # get the distance in cm using sonic speed (aprox. 34300 cm/s)
            distance = (elapsedTime * 34300) / 2

        GPIO.cleanup([self.trig, self.echo])
    
        return distance
from servokit import ServoKit
kit = ServoKit()
angle_x =250
angle_y = 400
kit.angle(6,int(angle_x))
kit.angle(7, int(angle_y))
rightMotor = Motor(32,21,19)
leftMotor = Motor(33,26,24)
speed = 100
    
leftMotor.setSpeed(speed)
rightMotor.setSpeed(speed)
def motor_con(move):
    
    if move == "goforward":
        leftMotor.goForward()
        rightMotor.goForward()
    elif move == 'gobackward':
        leftMotor.goBackward()
        rightMotor.goBackward()
    elif move == 'goleft':
        leftMotor.stop()
        speed = 100
              
        rightMotor.setSpeed(speed)
        rightMotor.goForward()
      
    elif move == 'goright':
        speed = 100
        leftMotor.setSpeed(speed)
        leftMotor.goForward()
        rightMotor.stop()
    elif move == 'stop':
        leftMotor.stop()
        rightMotor.stop()
    






def main_roboAI():
    from servokit import ServoKit
    kit = ServoKit()
    kit.angle(6, 250)
    kit.angle(7, 400)

    dis = DistanceSensor()
    move= True
    while move:
        
    
        data = dis.getDistance()
        print(data)
    
        if data == -1:
            continue
        if data < 25:
            print('stop')
            motor_con('stop')
        if data >25:
            #print(data)
            #print("goForward")
            motor_con('goforward')
        elif data < 25: 
            print("stop")
            #setServoAngle(0)
            #time.sleep(1)
            kit.angle(6, 100)
            kit.angle(7, 400)
            time.sleep(1)
            left_dis = dis.getDistance()
            #setServoAngle(90)
            
            #setServoAngle(180)
            #time.sleep(1)
            kit.angle(6, 350)
            kit.angle(7, 400)
            time.sleep(1)
            right_dis = dis.getDistance()
            #setServoAngle(90)
            kit.angle(6, 250)
            kit.angle(7, 400)

            if left_dis and right_dis< 15:
                print("gobackword")
                motor_con('gobackward')
                time.sleep(3)
            elif left_dis > right_dis:
                print("goleft")
                motor_con('goleft')

                time.sleep(5)
                
            elif left_dis < right_dis:
                print('goright')
                motor_con('goright')
                time.sleep(5)
              

        else:
            #print('stop')
            motor_con('stop')

                


  
if __name__ == "__main__":
    #move_ret(1)
    main_roboAI()
