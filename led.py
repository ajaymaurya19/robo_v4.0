import time
import RPi.GPIO as GPIO 
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BOARD)  # choose BCM numbering scheme.  
red = 11
green = 7
blue = 13

GPIO.setup(red, GPIO.OUT)# set GPIO 17 as output for white led  
GPIO.setup(green, GPIO.OUT)# set GPIO 27 as output for red led  
GPIO.setup(blue, GPIO.OUT)# set GPIO 22 as output for red led

def led_grb(color):
        if color == 'green':
                print('green')
                GPIO.output(red, GPIO.LOW) 
                GPIO.output(blue, GPIO.LOW) 
                GPIO.output(green, GPIO.HIGH)
        elif color == 'red':
                print('red')
                GPIO.output(blue, GPIO.LOW) 
                GPIO.output(green, GPIO.LOW)
                GPIO.output(red, GPIO.HIGH)
        elif color == 'blue':
                print('blue')
                GPIO.output(green, GPIO.LOW)
                GPIO.output(red, GPIO.LOW)
                GPIO.output(blue, GPIO.HIGH) 
                 
        elif color == 'pink':
                print('pink')
                GPIO.output(green, GPIO.LOW)
                GPIO.output(blue, GPIO.HIGH)
                GPIO.output(red, GPIO.HIGH)
                 
        elif color == 'yellow':
                print('yellow')
                GPIO.output(blue, GPIO.LOW)
                GPIO.output(green, GPIO.HIGH)
                GPIO.output(red, GPIO.HIGH)
                 
        elif color == 'aque':
                print('aque')
                GPIO.output(red, GPIO.LOW)
                GPIO.output(green, GPIO.HIGH)
                GPIO.output(blue, GPIO.HIGH) 
        elif color == 'magenta':
                print('magenta')
                GPIO.output(green, GPIO.LOW)
                GPIO.output(blue, GPIO.HIGH)
                GPIO.output(red, GPIO.HIGH)
        elif color == 'white':
                print('white')
                GPIO.output(green, GPIO.HIGH)
                GPIO.output(red, GPIO.HIGH)
                GPIO.output(blue, GPIO.HIGH)

if __name__ == '__main__':
        colors = ['red', 'blue', 'green', 'pink', 'aque', 'yellow', 'white', 'magenta']
        for color in colors:

                led_grb(color)
                time.sleep(5) 
               