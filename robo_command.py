
"""
Project: Python Based AI Voice Assistant
@author: Akshay Dattatray Khare
"""
import robo_tts
import datetime 
from datetime import date
import calendar
import time
import math

import webbrowser
import os

import pyautogui
import cv2
conn = connect("voice_assistant_asked_questions.db")

conn.execute("CREATE TABLE IF NOT EXISTS `voicedata`(id INTEGER PRIMARY KEY AUTOINCREMENT,command VARCHAR(201))")

conn.execute("CREATE TABLE IF NOT EXISTS `review`(id INTEGER PRIMARY KEY AUTOINCREMENT, review VARCHAR(50), type_of_review VARCHAR(50))")

conn.execute("CREATE TABLE IF NOT EXISTS `emoji`(id INTEGER PRIMARY KEY AUTOINCREMENT,emoji VARCHAR(201))")

global query
    
def detect_face():
    cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frames = video_capture.read()

        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
                )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frames)
        robo_tts.talk_gtts("detecting face")
        print("Detecting face.....")
        time.sleep(10)      
        pyautogui.press('q')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
from tkinter import *
import tkinter.messagebox as message
from sqlite3 import *
if __name__ == "__main__":
    detect_face()
    wishMe()
    said = True
    while said:

        query = take_command().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            robo_tts.talk_gtts('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            robo_tts.talk_gtts("According to Wikipedia")
            print(results)
            robo_tts.talk_gtts(results)
     

        
            
      
            
        elif 'face' in query and ('detect' in query or 'identif' in query or 'point' in query or 'highlight' in query or 'focus' in query):
            robo_tts.talk_gtts('yes')
            detect_face()

                           
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            robo_tts.talk_gtts(f"Sir, the time is {strTime}")
            
        elif 'open' in query and 'sublime' in query:
            path = "C:\Program Files\Sublime Text 3\sublime_text.exe"
            os.startfile(path)
        elif 'image' in query:
            path = "C:\Program Files\Internet Explorer\images"
            os.startfile(path)      
            
        elif 'quit' in query:
            robo_tts.talk_gtts('Ok, Thank you Sir.')
            said = False
            robo_tts.talk_gtts('Please give the review. It will help me to improve my performance.')
            select_review()
            
        elif 'exit' in query:
            robo_tts.talk_gtts('Ok, Thank you Sir.')
            said = False
            robo_tts.talk_gtts('Please give the review. It will help me to improve my performance.')
            select_review()
            
        elif 'stop' in query:
            robo_tts.talk_gtts('Ok, Thank you Sir.')
            said = False
            robo_tts.talk_gtts('Please give the review. It will help me to improve my performance.')
            select_review()
            
        elif 'shutdown' in query or 'shut down' in query:
            robo_tts.talk_gtts('Ok, Thank you Sir.')
            said = False
            robo_tts.talk_gtts('Please give the review. It will help me to improve my performance.')
            select_review()
            
        elif 'close you' in query:
            robo_tts.talk_gtts('Ok, Thank you Sir.')
            said = False
            robo_tts.talk_gtts('Please give the review. It will help me to improve my performance.')
            select_review()
            try:
                conn.execute(f"INSERT INTO `voice_assistant_review`(review, type_of_review) VALUES('{review}', '{type_of_review}')")
                conn.commit()                
            except Exception as e:
                pass
        elif 'bye' in query:
            robo_tts.talk_gtts('Bye Sir')
            said = False
            robo_tts.talk_gtts('Please give the review. It will help me to improve my performance.')
            select_review()
            
        elif 'wait' in query or 'hold' in query:
            
            robo_tts.talk_gtts('for how many seconds or minutes I have to wait?')
            query = take_command().lower()
            if 'second' in query:
                query = query.replace("please","")
                query = query.replace("can","")
                query = query.replace("you","")
                query = query.replace("have","")
                query = query.replace("could","")
                query = query.replace("hold","")
                query = query.replace("one","1")
                query = query.replace("only","")                
                query = query.replace("wait","")                
                query = query.replace("for","")                
                query = query.replace("the","")
                query = query.replace("just","")
                query = query.replace("seconds","")
                query = query.replace("second","")
                query = query.replace("on","")
                query = query.replace("a","")
                query = query.replace("to","")
                query = query.replace(" ","")
                #print(f'query:{query}')
                
                if query.isdigit() == True:
                    #print('y')
                    robo_tts.talk_gtts('Ok sir')
                    query = int(query)
                    time.sleep(query)
                    robo_tts.talk_gtts('my waiting time is over')
                else:
                    print('sorry sir. I unable to complete your request.')
            elif 'minute' in query:
                query = query.replace("please","")
                query = query.replace("can","")
                query = query.replace("you","")
                query = query.replace("have","")
                query = query.replace("could","")
                query = query.replace("hold","")
                query = query.replace("one","1")
                query = query.replace("only","")
                query = query.replace("on","")
                query = query.replace("wait","")                
                query = query.replace("for","")
                query = query.replace("the","")
                query = query.replace("just","")
                query = query.replace("and","")
                query = query.replace("half","")                
                query = query.replace("minutes","")
                query = query.replace("minute","")
                query = query.replace("a","")
                query = query.replace("to","")
                query = query.replace(" ","")
                #print(f'query:{query}')
                                
                if query.isdigit() == True:
                    #print('y')
                    robo_tts.talk_gtts('ok sir')
                    query = int(query)
                    time.sleep(query*60)
                    robo_tts.talk_gtts('my waiting time is over')
                else:
                    print('sorry sir. I unable to complete your request.')

     
      
        
        elif 'calculat' in query:
            robo_tts.talk_gtts('Yes. Which kind of calculation you want to do? add, substract, divide, multiply or anything else.')
            query = take_command().lower()
            calculator()
            
        
            robo_tts.talk_gtts('Mr. Akshay Dattatray Khare is my inventor. He is 19 years old and he is pursuing second year of engineering in Vishwakarma Institute of technology, Pune')
        elif 'your inventor' in query:
            robo_tts.talk_gtts('Mr. Akshay Dattatray Khare is my inventor')
        elif 'your creator' in query:
            robo_tts.talk_gtts('Mr. Akshay Dattatray Khare is my creator')
        elif 'invent you' in query:
            robo_tts.talk_gtts('Mr. Akshay Dattatray Khare invented me')
        elif 'create you' in query:
            robo_tts.talk_gtts('Mr. Akshay Dattatray Khare created me') 
       
        elif 'write' in query and 'your' in query and 'name' in query:
            print('Akshu2020')  
            pyautogui.write('Akshu2020') 
        elif 'write' in query and ('I' in query or 'whatever' in query) and 'say' in query:
            robo_tts.talk_gtts('Ok sir I will write whatever you will say. Please put your cursor where I have to write.......Please Start robo_tts.talk_gttsing now sir.')
            query = take_command().lower()
            pyautogui.write(query) 
       
        elif ('repeat' in query and ('word' in query or 'sentence' in query or 'line' in query) and ('say' in query or 'tell' in query)) or ('repeat' in query and 'after' in query and ('me' in query or 'my' in query)):
            robo_tts.talk_gtts('yes sir, I will repeat your words starting from now')
            query = take_command().lower()
            robo_tts.talk_gtts(query)
            time.sleep(1)
            robo_tts.talk_gtts("If you again want me to repeat something else, try saying, 'repeat after me' ")
            
        elif ('send' in query or 'sent' in query) and ('mail' in query or 'email' in query or 'gmail' in query):
            try:
                robo_tts.talk_gtts('Please enter the email id of receiver.')
                to = input("Enter the email id of reciever: ")
                robo_tts.talk_gtts(f'what should I say to {to}')
                content = take_command()
                sendEmail(to, content)
                robo_tts.talk_gtts("Email has been sent")
            except Exception as e:
                #print(e)
                robo_tts.talk_gtts("sorry sir. I am not able to send this email")
        elif 'currency' in query and 'conver' in query:
            robo_tts.talk_gtts('I can convert, US dollar into indian rupee, and indian rupee into US dollar. Do you want to continue it?')
            query = take_command().lower()
            if 'y' in query or 'sure' in query or 'of course' in query:
                robo_tts.talk_gtts('which conversion you want to do? US dollar to indian rupee, or indian rupee to US dollar?')
                query = take_command().lower()
                if ('dollar' in query or 'US' in query) and ('to india' in query or 'to rupee' in query):
                    robo_tts.talk_gtts('Enter US Dollar')  
                    USD = float(input("Enter United States Dollar (USD):"))                                     
                    INR = USD * 74.8
                    inr = "{:.4f}".format(INR)
                    print(f"{USD} US Dollar is equal to {inr} indian rupee.")
                    robo_tts.talk_gtts(f'{USD} US Dollar is equal to {inr} indian rupee.')
                    robo_tts.talk_gtts("If you again want to do currency conversion then say, 'convert currency' " )
                elif ('india' in query or 'rupee' in query) and ('to US' in query or 'to dollar' in query or 'to US dollar'):
                    robo_tts.talk_gtts('Enter Indian Rupee')
                    INR = float(input("Enter Indian Rupee (INR):"))                                       
                    USD = INR/74.8
                    usd = "{:.3f}".format(USD)
                    print(f"{INR} indian rupee is equal to {usd} US Dollar.")
                    robo_tts.talk_gtts(f'{INR} indian rupee is equal to {usd} US Dollar.')
                    robo_tts.talk_gtts("If you again want to do currency conversion then say, 'convert currency' " )
                else:
                    robo_tts.talk_gtts("I cannot understand what did you say. If you want to convert currency just say 'convert currency'")
            else:
                print('ok sir')
            
        elif 'about you' in query:
            robo_tts.talk_gtts('My name is akshu2020. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device. I am also able to send email')             
        elif 'your intro' in query:
            robo_tts.talk_gtts('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')            
        elif 'your short intro' in query:
            robo_tts.talk_gtts('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.') 
        elif 'your quick intro' in query:
            robo_tts.talk_gtts('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.') 
        elif 'your brief intro' in query:
            robo_tts.talk_gtts('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.') 
        elif 'you work' in query:
            robo_tts.talk_gtts('run the program and say what do you want. so that I can help you. In this way I work')
        elif 'your job' in query:
            robo_tts.talk_gtts('My job is to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')    
        elif 'your work' in query:
            robo_tts.talk_gtts('My work is to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')    
        elif 'work you' in query:
            robo_tts.talk_gtts('My work is to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.') 
        elif 'your information' in query:
            robo_tts.talk_gtts('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')
        elif 'yourself' in query:
            robo_tts.talk_gtts('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')
        elif 'introduce you' in query:
            robo_tts.talk_gtts('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')           
        elif 'description' in query:
            robo_tts.talk_gtts('My name is akshu2020. Version 1.0. Mr. Akshay Khare is my inventor. I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')
        elif 'your birth' in query:
            robo_tts.talk_gtts('My birthdate is 6 August two thousand twenty')
        elif 'your use' in query:
            robo_tts.talk_gtts('I am able to send email and play music. I can do mathematical calculations. I can also open youtube, google and some apps or software in your device.')
        elif 'you eat' in query:
            robo_tts.talk_gtts('I do not eat anything. But the device in which I do my work requires electricity to eat')
        elif 'your food' in query:
            robo_tts.talk_gtts('I do not eat anything. But the device in which I do my work requires electricity to eat')
        elif 'you live' in query:
            robo_tts.talk_gtts('I live in India, in laptop of Mr. Akshay Khare') 
        elif 'where from you' in query:
            robo_tts.talk_gtts('I am from India, I live in laptop of Mr. Akshay Khare')
        elif 'you sleep' in query:
            robo_tts.talk_gtts('Yes,  when someone close this program or stop to run this program then I sleep and again wake up when someone again run me.')
        elif 'what are you doing' in query:
            robo_tts.talk_gtts('Talking with you.')
        elif 'you communicate' in query:
            robo_tts.talk_gtts('Yes, I can communicate with you.')
        elif 'hear me' in query:
            robo_tts.talk_gtts('Yes sir, I can hear you.')
        elif 'you' in query and 'dance' in query:
            robo_tts.talk_gtts('No, I cannot dance.')
        elif 'tell' in query and 'joke' in query:
            robo_tts.talk_gtts("Ok, here's a joke")
            robo_tts.talk_gtts("'Write an essay on cricket', the teacher told the class. Chintu finishes his work in five minutes. The teacher is impressed, she asks chintu to read his essay aloud for everyone. Chintu reads,'The match is cancelled because of rain', hehehehe,haahaahaa,hehehehe,haahaahaa")
        
        elif 'your' in query and 'favourite' in query:
            if 'actor' in query:
                robo_tts.talk_gtts('Amitaabh Bachchaan, is my favourite actor.')
            elif 'food' in query:
                robo_tts.talk_gtts('I can always go for some food for thought. Like facts, jokes, or interesting searches, we could look something up now')
            elif 'country' in query:
                robo_tts.talk_gtts('India')
            elif 'city' in query:
                robo_tts.talk_gtts('pune')
            elif 'dancer' in query:
                robo_tts.talk_gtts('Michael jackson')
            elif 'singer' in query:
                robo_tts.talk_gtts('lataa mangeshkar, is my favourite singer.')
            elif 'movie' in query:
                robo_tts.talk_gtts('Taarre Zameen paar, such a treat')
        
        elif 'sing a song' in query:
            robo_tts.talk_gtts('I cannot sing a song. But I know the 7 sur in indian music, saaareeegaaamaaapaaadaaanisaa')
        
        
        elif 'day after tomorrow' in query or 'date after tomorrow' in query:
            td = datetime.date.today() + datetime.timedelta(days=2)
            print(td)
            robo_tts.talk_gtts(td)
        elif 'day before today' in query or 'date before today' in query or 'yesterday' in query or 'previous day' in query:
            td = datetime.date.today() + datetime.timedelta(days= -1)
            print(td)
            robo_tts.talk_gtts(td)
        elif ('tomorrow' in query and 'date' in query) or 'what is tomorrow' in query or (('day' in query or 'date' in query) and 'after today' in query):
            td = datetime.date.today() + datetime.timedelta(days=1)
            print(td)
            robo_tts.talk_gtts(td)
        elif 'month' in query or ('current' in query and 'month' in query):
            current_date = date.today()
            m = current_date.month
            month = calendar.month_name[m]
            print(f'Current month is {month}')
            robo_tts.talk_gtts(f'Current month is {month}')
        elif 'date' in query or ('today' in query and 'date' in query) or 'what is today' in query or ('current' in query and 'date' in query):
            current_date = date.today()           
            print(f"Today's date is {current_date}")
            robo_tts.talk_gtts(f'Todays date is {current_date}')
            
        elif 'year' in query or ('current' in query and 'year' in query):
            current_date = date.today()
            m = current_date.year
            print(f'Current year is {m}')
            robo_tts.talk_gtts(f'Current year is {m}')
        
        
   
 
       #answer is wrong' 
        
        #'answer is incorrect'
            
        #'answer is totally wrong'
        
        #'wrong answer'
        
        #'incorrect answer'
        
        #'answer is totally incorrect'
        
        #'answer is incomplete'
        
        #'incomplete answer'
        
        #'answer is improper'
        
        #'answer is not correct'
        
        #'answer is not complete'
        
        #'answer is not yet complete'
        
        #'answer is not proper'
        
        #'t gave me proper answer'
        
        #'t giving me proper answer'
        
        #'t gave me complete answer'
        
        #'t giving me complete answer'
        
        #'t given me proper answer'
        
        #'t given me complete answer'
        
        #'t gave me correct answer'
        
        #'t giving me correct answer'
        
        #'t given me correct answer'
        #'I am sorry Sir. I searched your question in wikipedia and thats  why I told you this answer.')
        
      
        
                
        
        elif 'information' in query:
            try:
                robo_tts.talk_gtts('Information about what?')
                query = take_command().lower()
                #robo_tts.talk_gtts('Searching wikipedia...')
                query = query.replace("information","")
                results = wikipedia.summary(query, sentences=3)
                #robo_tts.talk_gtts("According to Wikipedia")
                print(results)
                robo_tts.talk_gtts(results)
            except Exception as e:
                robo_tts.talk_gtts('I am not able to answer your question.')
               
            
        elif 'something about ' in query:
            try:
                #robo_tts.talk_gtts('Searching wikipedia...')
                query = query.replace("something about ","")
                results = wikipedia.summary(query, sentences=3)
                #robo_tts.talk_gtts("According to Wikipedia")
                print(results)
                robo_tts.talk_gtts(results)
            except Exception as e:
                robo_tts.talk_gtts('I unable to answer your question.')
                
                
        elif 'tell me about ' in query:
            try:
                #robo_tts.talk_gtts('Searching wikipedia...')
                query = query.replace("tell me about ","")
                results = wikipedia.summary(query, sentences=3)
                #robo_tts.talk_gtts("According to Wikipedia")
                print(results)
                robo_tts.talk_gtts(results)
            except Exception as e:
                robo_tts.talk_gtts('I am unable to answer your question.')
                
                
      
                
        
        elif 'alarm' in query:
            alarm()
        elif 'bharat mata ki' in query:
            robo_tts.talk_gtts('jay')
        elif 'kem chhe' in query:
            robo_tts.talk_gtts('majaama')
        elif 'namaskar' in query:
            robo_tts.talk_gtts('Namaskaar')
        elif 'jo bole so nihal' in query:
            robo_tts.talk_gtts('sat shri akaal')
        elif 'jay hind' in query:
            robo_tts.talk_gtts('jay bhaarat')
        elif 'jai hind' in query:
            robo_tts.talk_gtts('jay bhaarat')
       
        elif 'hip hip' in query:
            robo_tts.talk_gtts('Hurreh')
        elif 'help' in query:
            robo_tts.talk_gtts('I will try my best to help you if I have solution of your problem.')
        elif 'follow' in query:
            robo_tts.talk_gtts('Ok sir')
        elif 'having illness' in query:
            robo_tts.talk_gtts('Take care and get well soon')
        elif 'today is my birthday' in query:
            robo_tts.talk_gtts('many many happy returns of the day. Happy birthday.')
            print("???? Happy Birthday ????")
        elif 'you are awesome' in query:
            robo_tts.talk_gtts('Thank you sir. It is because of artificial intelligence which had learnt by humans.')
        elif 'you are great' in query:
            robo_tts.talk_gtts('Thank you sir. It is because of artificial intelligence which had learnt by humans.')
        
        elif 'laugh' in query:
            robo_tts.talk_gtts('hehehehe,haahaahaa,hehehehe,haahaahaa,hehehehe,haahaahaa')
            print('????')
       
                
   
            
     
            
        elif 'play' in query or 'turn on' in query and ('music' in query or 'song' in query) :
           try:
               music_dir = 'C:\\Users\\Admin\\Music\\Playlists'
               songs = os.listdir(music_dir)
               print(songs)
               os.startfile(os.path.join(music_dir, songs[0]))
           except Exception as e:
               #print(e)
               robo_tts.talk_gtts('Sorry sir, I am not able to play music')
            
        elif (('open' in query or 'turn on' in query) and 'camera' in query) or (('click' in query or 'take' in query) and ('photo' in query or 'pic' in query)):
            robo_tts.talk_gtts("Opening camera")
            cam = cv2.VideoCapture(0)

            cv2.namedWindow("test")

            img_counter = 0
            robo_tts.talk_gtts('say click, to click photo.....and if you want to turn off the camera, say turn off the camera')

            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    robo_tts.talk_gtts('failed to grab frame')
                    break
                cv2.imshow("test", frame)

                query = take_command().lower()
                k = cv2.waitKey(1)
                
                if 'click' in query or ('take' in query and 'photo' in query):
                    robo_tts.talk_gtts('Be ready!...... 3.....2........1..........')
                    pyautogui.press('space')
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    robo_tts.talk_gtts('{} written!'.format(img_name))
                    img_counter += 1
                elif 'escape' in query or 'off' in query or 'close' in query:
                    pyautogui.press('esc')
                    print("Escape hit, closing...")
                    robo_tts.talk_gtts('Turning off the camera')
                    break
                elif k%256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k%256 == 32:
        
                    # SPACE pressed
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    robo_tts.talk_gtts('{} written!'.format(img_name))
                    img_counter += 1
                elif 'exit' in query or 'stop' in query or 'bye' in query:
                    robo_tts.talk_gtts('Please say, turn off the camera or press escape button before giving any other command')
                else:
                    robo_tts.talk_gtts('I did not understand what did you say or you entered a wrong key.')

            cam.release()

            cv2.destroyAllWindows()
            
            
        elif 'screenshot' in query:
            robo_tts.talk_gtts('Please go on the screen whose screenshot you want to take, after 5 seconds I will take screenshot')
            time.sleep(4)
            robo_tts.talk_gtts('Taking screenshot....3........2.........1.......')
            pyautogui.screenshot('screenshot_by_akshu2020.png') 
            robo_tts.talk_gtts('The screenshot is saved as screenshot_by_akshu2020.png')
        elif 'click' in query and 'start' in query:
            pyautogui.moveTo(10,1200)    
            pyautogui.click()
        elif ('open' in query or 'click' in query) and 'calendar' in query:
            pyautogui.moveTo(1800,1200)   
            pyautogui.click() 
        elif 'minimise' in query and 'screen' in query:
            pyautogui.moveTo(1770,0)   
            pyautogui.click()
        elif 'increase' in query and ('volume' in query or 'sound' in query):
            pyautogui.press('volumeup') 
        elif 'decrease' in query and ('volume' in query or 'sound' in query):
            pyautogui.press('volumedown')
        elif 'capslock' in query or ('caps' in query and 'lock' in query):
            pyautogui.press('capslock')
        elif 'mute' in query:
            pyautogui.press('volumemute')
      
            
         
        
            
            
        elif 'me the answer' in query:
            robo_tts.talk_gtts('Yes sir, I will try my best to answer you.')
        elif 'me answer' in query or ('answer' in query and 'question' in query):
            robo_tts.talk_gtts('Yes sir, I will try my best to answer you.')
      
        elif 'can you' in query or 'could you' in query:
            robo_tts.talk_gtts('I will try my best if I can do that.')
        elif 'do you' in query:
            robo_tts.talk_gtts('I will try my best if I can do that.')
        elif 'truth' in query:
            robo_tts.talk_gtts('I always robo_tts.talk_gtts truth. I never lie.')
        elif 'true' in query:
            robo_tts.talk_gtts('I always robo_tts.talk_gtts truth. I never lie.')        
        elif 'lying' in query:
            robo_tts.talk_gtts('I always robo_tts.talk_gtts truth. I never lie.')
        elif 'liar' in query:
            robo_tts.talk_gtts('I always robo_tts.talk_gtts truth. I never lie.')    
        elif 'doubt' in query:
            robo_tts.talk_gtts('I will try my best if I can clear your doubt.')
            
        elif ' by' in query:
            robo_tts.talk_gtts('If you want to do any mathematical calculation then give me a command to open calculator.')
     
        elif 'nonsense' in query: 
            robo_tts.talk_gtts("I'm sorry sir")
        elif 'mad' in query:
            robo_tts.talk_gtts("I'm sorry sir") 
        elif 'shut up' in query:
            robo_tts.talk_gtts("I'm sorry sir")
        elif 'nice' in query:
            robo_tts.talk_gtts('Thank you sir')
        elif 'good' in query or 'wonderful' in query or 'great' in query:
            robo_tts.talk_gtts('Thank you sir')
        elif 'excellent' in query:
            robo_tts.talk_gtts('Thank you sir')
        elif 'ok' in query:
            robo_tts.talk_gtts('Hmmmmmm')
        

        elif 'akshu 2020' in query:
            robo_tts.talk_gtts('yes sir')
                   
        elif len(query) >= 200:
            robo_tts.talk_gtts('Your voice is pretty good!')  
       
                
                
        else:
            robo_tts.talk_gtts('I unable to give answer of your question')
        try:
            conn.execute(f"INSERT INTO `voicedata`(command) VALUES('{query}')")
            conn.commit()                
        except Exception as e:
            pass
   