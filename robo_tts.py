import speech_recognition as sr
import pyttsx3
import  os
import RPi.GPIO as GPIO
import time
from gtts import gTTS
from googletrans import Translator
from playsound import playsound  
import led
import datetime
import json

   
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voice_data =""
translator = Translator()

def stringtolist(string):
    listres = list(string.split(" "))
    return listres
def talk_gtts(text_val,language):
    
    language = language 
    obj = gTTS(text=text_val, lang=language, slow=False)
    obj.save("exam.mp3")  
    playsound("exam.mp3")
    os.remove("exam.mp3")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        
        led.led_grb('green')
     
        r.energy_threshold += 280
        # # print(r.adjust_for_ambient_noise(source,duration=1))
        audio = r.listen(source)
        led.led_grb('red')
        
    
        # Speech recognition using Google Speech Recognition
    try:
        #print("Parsing ...")  # Debugging To
        voice_data = r.recognize_google(audio)
        '''output_language = translator.translate(voice_data)
        language = output_language.src
        if language != 'en':
            voice_data = output_language.text
            print(voice_data)'''
        language = "en"
        #return voice_data.lower(), language  # returning the text which has been inputed.
        #angle(100, 60)
        return voice_data.lower()

    except sr.UnknownValueError:
        pass
    
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
def change_language(S_text, language):
    trans3 = translator.translate(S_text,dest = language)
    print(trans3.text)
    talk_gtts(trans3.text,language)
if  __name__ == "__main__":
   
    talk_gtts('hello i am robo','en')
    while True:
        
        print('hi')
        text = take_command()
        print(text)
        '''if text == 'nothing':
            pass
        else:
            print(text)
            if text == 'yes':
                angle(100, 60)
                angle(80, 60)
                angle(100, 60)
                angle(80, 60)
            elif text == "no":
                angle(100, 45)
                angle(100, 90)
                angle(100, 45)
                angle(100, 90)
            elif text == "hello":
                time = datetime.datetime.now().strftime('%I:%M%p')


                # the file to be converted
                filename = "/media/password/nvidia/robo_AI/semples.txt"

                # resultant dictionary
                dict1 = {}

                l =0

                with open(filename) as fh:
                    
                    f1 = fh.readlines()
                    f1 = [s.rstrip('\n') for s in f1]
                    l =0
                    #y = ''
                    for x in f1:
                        dict2 = {}
                        print(x)
                        talk_gtts(x,'en')
                        sno ='emp'+str(l)
                        y = take_command()
                        dictionary ={
                                    "tag": sno,
                                    "patterns": [ list(x.split(', '))],
                                    "responses": [
                                            y
                                    ]
                                
                                }
                        l = l+1
                        #dict1[sno]= dictionary
                        print(dictionary)

                        # creating json file		
                        out_file = open(f"/media/robo/nvidia/robo_AI/data_{time}.json", "w")
                        json.dump(dictionary, out_file, indent = 4)
                        out_file.close()

                

            else:
                pass'''

            

            



