import Adafruit_PCA9685
import time
#from guizero import App, Box, Text, PushButton, Slider



class ServoKit:
    def __init__(self) -> None:

        self.pwm = Adafruit_PCA9685.PCA9685(address = 0x40, busnum = 1)
        # Number of servo
        self.servo_num = 12

        # Configure min and max servo pulse lengths
        self.servo_min    = 100 # min. pulse length
        self.servo_max    = 600 # max. pulse length
        self.servo_offset = 400


# Set frequency to 60[Hz]
        self.pwm.set_pwm_freq(60)
    def angle(self,channel, angle):
        #kit.servo[7].angle=int(slider_value)
        self.slider_value = angle
        self.channel = channel

        self.pwm.set_pwm(self.channel, 0, self.servo_min+int(self.slider_value))
        #time.sleep(1)

if __name__ == "__main__":
    servo = ServoKit()
    def ServoPosition7(slider_value):
        servo.angle(7,int(slider_value))
    app = App(title="Servo GUI", width=500, height=550, layout="auto")
    reading_text = Text(app, text="Servo 7 left right")
    servo_position = Slider(app, command=ServoPosition7, start=1, end=180, width='fill')

    app.display()