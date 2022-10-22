from pickle import NONE



from neuralintents import GenericAssistant
import datetime
import googlesamples.assistant.grpc.pushtotalk as pushtotalk
import speech_recognition as sr
import pyttsx3
import webbrowser
#import pywhatkit
import datetime
import  os
import random

import re
import requests

from os import path
import subprocess
from gtts import gTTS

from robo_tts import take_command, talk, change_language, talk_gtts




def function_for_greetings():
    print("You triggered the greetings intent!")
    # Some action you want to take

def function_for_stocks():
    print("You triggered the stocks intent!")
    # Some action you want to take
def time__now():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Hello,Good Morning")

    elif hour>=12 and hour<18:
        print("Hello,Good Afternoon")

    else:
        print("Hello,Good Evening")

def time_now():
    time = datetime.datetime.now().strftime('%I:%M %p')
    S_text = 'Current time is ' + time
    if language != 'en':
        change_language(S_text, language)
    else:
        talk(S_text)

def call():
    print("hi")


def exit():
    #elif 'exit' in voice_data or "goodbye" in voice_data or "ok bye" in voice_data or "stop" in voice_data:
    print('Your robo is shutting down,Good bye')
    S_text = 'your robo is shutting down,Good bye'
    exit()
def log_off():
 
    shut=take_command()
    if shut == 'yes':
        print("Ok , your pc will log off in 10 sec make sure you exit from all applications")
        S_text = "Ok , your pc will log off in 10 sec make sure you exit from all applications"
        subprocess.call(["shutdown", "/l"])
    else:
        pass

path_of_startup ='/media/robo/nvidia/Robo_3.0/startup.txt'
path_of_json = '/media/robo/nvidia/Robo_3.0/Intent1.json'
path_of_model = '/media/robo/nvidia/Robo_3.0/neuralintents/test_model.h5'


mappings = {'greeting' : function_for_greetings, 'stocks' : function_for_stocks, 'TimeQuery' : time_now}

assistant = GenericAssistant(path_of_json, intent_methods=mappings ,model_name=path_of_model)
assistant.train_model()
assistant.save_model()
assistant.load_model(path_of_model)


if __name__ == "__main__":
    with open(path_of_startup, "r") as m:
        sents = m.read().split("\n\n")
        se = random.choice(sents)
    print(se)
    talk_gtts(se,'en')
    try:
        while True:
            messag = take_command()
            
            massage = messag[0]
            language = messag[1]
            if "rotate right" or "look right" in massage:
                print("looking right")
            elif "rotate left" or "look left" in massage:
                print("looking right")
            elif "detect this" in massage:
                print("detecting")
            elif "follow this" in massage:
                print("follow")
                
            print(massage)
            mess = assistant.request(massage)
            print(mess)
        
            if mess is NONE:
                pushtotalk.main()
    
            else:
                talk_gtts(mess,language)
                
                pushtotalk.main()
    except:
        pass

