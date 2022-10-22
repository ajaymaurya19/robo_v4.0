from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pan = 32
tilt = 33
GPIO.setup(tilt, GPIO.OUT) # white => TILT
GPIO.setup(pan, GPIO.OUT) # gray ==> PAN
def setServoAngle(servo, angle):
	assert angle >=30 and angle <= 150
	pwm = GPIO.PWM(servo, 50)
	pwm.start(8)
	dutyCycle = angle / 18. + 3.
	pwm.ChangeDutyCycle(dutyCycle)
	sleep(0.3)

	pwm.stop()
if __name__ == '__main__':
	import sys
	if len(sys.argv) == 1:
		setServoAngle(pan, 90)
		setServoAngle(tilt, 70)
	else:
		setServoAngle(pan, int(sys.argv[1])) # 30 ==> 90 (middle point) ==> 150
		setServoAngle(tilt, int(sys.argv[2])) # 30 ==> 90 (middle point) ==> 150
	GPIO.cleanup()