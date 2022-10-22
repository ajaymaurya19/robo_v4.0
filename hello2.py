from flask import Flask, render_template, request, redirect, url_for, make_response
from robo_move3 import *
rightMotor = Motor(16,13)
leftMotor = Motor(24,22)

app = Flask(__name__) #set up flask server
#when the root IP is selected, return index.html page
@app.route('/')
def index():
    return render_template('index.html')
#recieve which pin to change from the button press on index.html
#each button returns a number that triggers a command in this function
#
#Uses methods from motors.py to send commands to the GPIO to operate the motors
@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    changePin = int(changepin) #cast changepin to an int
    if changePin == 2:
        print ('Left')
        leftMotor.goForward()
        rightMotor.stop()
       
    elif changePin == 1:
        print ('Forward')
        leftMotor.goForward()
        rightMotor.goForward()
             
    elif changePin == 4:
        print ('Right')
        leftMotor.stop()
        rightMotor.goForward()
              
    elif changePin == 5:
        print ('Reverse')
        leftMotor.goBackward()
        rightMotor.goBackward()
    elif changePin == 3:
        print ('Reverse')
        leftMotor.stop()
        rightMotor.stop()
              
    else:
        print('stop')
        
    response = make_response(redirect(url_for('index')))
    return(response)
app.run(debug=True, host='192.168.43.136', port=8001) #set up the server in debug mode to the port 8000