from playsound import playsound  
#playsound('/media/robo/nvidia/database/robo.mp3', True)
import os
import logging
import json

import calendar
from pickle import NONE

from nltk.util import pr

from neuralintents import GenericAssistant
import datetime

import random
from os import path
import subprocess
from robo_tts import take_command, talk, change_language, talk_gtts
import multiprocessing as mp
from threading import Thread

import click
import google.auth.transport.grpc
import google.auth.transport.requests
import google.oauth2.credentials

print('loading.....')
from google.assistant.embedded.v1alpha2 import (
    embedded_assistant_pb2,
    embedded_assistant_pb2_grpc
)

try:
    from googlesamples.assistant.grpc import (
        assistant_helpers,
        browser_helpers,
    )
except (SystemError, ImportError):
    import googlesamples.assistant.grpc.assistant_helpers
    import googlesamples.assistant.grpc.browser_helpers

global query

ASSISTANT_API_ENDPOINT = 'embeddedassistant.googleapis.com'
DEFAULT_GRPC_DEADLINE = 60 * 3 + 5
PLAYING = embedded_assistant_pb2.ScreenOutConfig.PLAYING


class SampleTextAssistant(object):


    def __init__(self, language_code, device_model_id, device_id,
                 display, channel, deadline_sec):
        self.language_code = language_code
        self.device_model_id = device_model_id
        self.device_id = device_id
        self.conversation_state = None
        # Force reset of first conversation.
        self.is_new_conversation = True
        self.display = display
        self.assistant = embedded_assistant_pb2_grpc.EmbeddedAssistantStub(
            channel
        )
        self.deadline = deadline_sec

    def __enter__(self):
        return self

    def __exit__(self, etype, e, traceback):
        if e:
            return False

    def assist(self, text_query):
        """Send a text request to the Assistant and playback the response.
        """
        def iter_assist_requests():
            config = embedded_assistant_pb2.AssistConfig(
                audio_out_config=embedded_assistant_pb2.AudioOutConfig(
                    encoding='LINEAR16',
                    sample_rate_hertz=16000,
                    volume_percentage=0,
                ),
                dialog_state_in=embedded_assistant_pb2.DialogStateIn(
                    language_code=self.language_code,
                    conversation_state=self.conversation_state,
                    is_new_conversation=self.is_new_conversation,
                ),
                device_config=embedded_assistant_pb2.DeviceConfig(
                    device_id=self.device_id,
                    device_model_id=self.device_model_id,
                ),
                text_query=text_query,
            )
            # Continue current conversation with later requests.
            self.is_new_conversation = False
            if self.display:
                config.screen_out_config.screen_mode = PLAYING
            req = embedded_assistant_pb2.AssistRequest(config=config)
            assistant_helpers.log_assist_request_without_audio(req)
            yield req

        text_response = None
        html_response = None
        for resp in self.assistant.Assist(iter_assist_requests(),
                                          self.deadline):
            assistant_helpers.log_assist_response_without_audio(resp)
            if resp.screen_out.data:
                html_response = resp.screen_out.data
            if resp.dialog_state_out.conversation_state:
                conversation_state = resp.dialog_state_out.conversation_state
                self.conversation_state = conversation_state
            if resp.dialog_state_out.supplemental_display_text:
                text_response = resp.dialog_state_out.supplemental_display_text
        return text_response, html_response


@click.command()
@click.option('--api-endpoint', default=ASSISTANT_API_ENDPOINT,
              metavar='<api endpoint>', show_default=True,
              help='Address of Google Assistant API service.')
@click.option('--credentials',
              metavar='<credentials>', show_default=True,
              default=os.path.join(click.get_app_dir('google-oauthlib-tool'),
                                   'credentials.json'),
              help='Path to read OAuth2 credentials.')
@click.option('--device-model-id',default=ASSISTANT_API_ENDPOINT,
              metavar='<device model id>',
              required=True,
              help=(('Unique device model identifier, '
                     'if not specifed, it is read from --device-config')))
@click.option('--device-id',default=ASSISTANT_API_ENDPOINT,
              metavar='<device id>',
              required=True,
              help=(('Unique registered device instance identifier, '
                     'if not specified, it is read from --device-config, '
                     'if no device_config found: a new device is registered '
                     'using a unique id and a new device config is saved')))
@click.option('--lang', show_default=True,
              metavar='<language code>',
              default='en-US',
              help='Language code of the Assistant')
@click.option('--display', is_flag=True, default=False,
              help='Enable visual display of Assistant responses in HTML.')
@click.option('--verbose', '-v', is_flag=True, default=False,
              help='Verbose logging.')
@click.option('--grpc-deadline', default=DEFAULT_GRPC_DEADLINE,
              metavar='<grpc deadline>', show_default=True,
              help='gRPC deadline in seconds')

def main(api_endpoint, credentials,
         device_model_id, device_id, lang, display, verbose,
         grpc_deadline, *args, **kwargs):
    # Setup logging.
    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO)

    # Load OAuth 2.0 credentials.
    try:
        with open(credentials, 'r') as f:
            credentials = google.oauth2.credentials.Credentials(token=None,
                                                                **json.load(f))
            http_request = google.auth.transport.requests.Request()
            credentials.refresh(http_request)
    except Exception as e:
        logging.error('Error loading credentials: %s', e)
        logging.error('Run google-oauthlib-tool to initialize '
                      'new OAuth 2.0 credentials.')
        return

    # Create an authorized gRPC channel.
    grpc_channel = google.auth.transport.grpc.secure_authorized_channel(
        credentials, http_request, api_endpoint)
    logging.info('Connecting to %s', api_endpoint)

    with SampleTextAssistant(lang, device_model_id, device_id, display,
                             grpc_channel, grpc_deadline) as assistant:
    
        #query = click.prompt('')
        #click.echo('<you> %s' % query)
        
        response_text, response_html = assistant.assist(text_query=query)
        if display and response_html:
            system_browser = browser_helpers.system_browser
            system_browser.display(response_html)
        if response_text:
            #click.echo('<@assistant> %s' % response_text)
            talk_gtts(response_text,"en")
            #print("google")




def move_cam():
    print("csm move")
def recogni():
    print("reco")
    q.put('face_reco')
def detect_cam():
    print("detect")
    q.put('detect')
def detect_stop():
    print("detection stop")
    q.put('detect stop')
def follow():
    print('follow')
def google_sdk():
    print("google sdk")
    query = message
    main()   
def look_right():
    print("looking right")
    kit.angle(6, 0)
    kit.angle(7, 130)
def time_now():
    time = datetime.datetime.now().strftime('%I:%M %p')
    S_text = 'Current time is ' + time
    talk_gtts(S_text,'en')

def current_year():
    current_date = date.today()
    m = current_date.year
    S_text = 'Current year is ' + m
    talk_gtts(S_text,'en')
    
    
def month_current():
    current_date = date.today()
    m = current_date.month
    month = calendar.month_name[m]
    S_text = 'Current year is ' + month
    talk_gtts(S_text,'en')

#elif ('tomorrow' in query and 'date' in query) or 'what is tomorrow' in query or (('day' in query or 'date' in query) and 'after today' in query):
def tomorrow():
    td = datetime.date.today() + datetime.timedelta(days=1)
    S_text = 'Current year is ' + td
    talk_gtts(S_text,'en')
    
    
  
def look_left():
    kit.angle(6, 180)
    kit.angle(7, 130)
def look_up():
    kit.angle(6, 180)
    kit.angle(7, 200)
def look_down():
    kit.angle(6, 180)
    kit.angle(7, 10)
def look_front():
    kit.angle(6, 100)
    kit.angle(7, 130)
def go_forward(): 
    while True:        
        data = dis.getDistance()
            #print(data)
       
        if data == -1:
            continue
        if data < 20:
            print('stop')
            leftMotor.stop()
            rightMotor.stop()
            break
        if data >20:
                #print(data)
            print("goForward")
            leftMotor.goForward()
            rightMotor.goForward()
      
def go_backward():
    leftMotor.goBackward()
    rightMotor.goBackward()
    #time.sleep(2)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        talk_gtts("Good Morning!",'en')
    elif hour >= 12 and hour < 18:
        talk_gtts("Good Afternoon!",'en')
    else:
        talk_gtts("Good Evening!",'en')
def greeting():
    playsound('/media/robo/nvidia/Robo_3.0/good.mp3', True)

    playsound('/media/robo/nvidia/Robo_3.0/college.mp3', True)
    playsound('/media/robo/nvidia/Robo_3.0/hello.mp3', True)
    playsound('/media/robo/nvidia/Robo_3.0/introd.mp3', True)

    playsound('/media/robo/nvidia/Robo_3.0/birth.mp3', True)

    kit.angle(0, 250)
    kit.angle(3, 250)
    time.sleep(15)
    kit.angle(3, 0)
    kit.angle(0, 500)
            

if __name__ == "__main__":
    q = mp.Queue() 
    #t3 = mp.Process(target= thred, args=(q,))
    #t1 = mp.Process(target= cam,args=(q,))
    
    #t2 = mp.Process(target=main_roboAI2, args=(q,))
    #t1.start()
    #t3.start()
    path_of_startup ='/media/robo/nvidia/Robo_3.0/startup.txt'
    path_of_json = '/media/robo/nvidia/Robo_3.0/Intent1.json'
    path_of_model = '/media/robo/nvidia/Robo_3.0/neuralintents/test_model.h5'


    mappings = {
                'TimeQuery' : time_now,
            
                "detect_comm" : detect_cam,
                "detect_stop" : detect_stop,
                "follow"  : follow,
                "look_right" : look_right,
                "look_left" : look_left,
                "look_up" : look_up,
                "look_down" : look_down,
                "goforward" : go_forward,
                "gobackward" : go_backward
                }
  
    assistant = GenericAssistant(path_of_json, intent_methods=mappings ,model_name=path_of_model)
    #assistant.train_model()
    #assistant.save_model()
    assistant.load_model(path_of_model)
    kit.angle(6, 250)
    kit.angle(7, 200)
  
    wishMe()
    with open(path_of_startup, "r") as m:
        sents = m.read().split("\n\n")
        se = random.choice(sents)
    print(se)
    talk_gtts(se,'en')
  

    while True:
        try:
            #parent_conn.send(['0'])
            print('listen...')
            #led.led_grb(('green'))
            message = take_command()
            #message = input('Enter..')
            #led.led_grb(('red'))
            if message is 'nothing':
                pass 
            print(message)
            if "reco" in message:
                q.put('face_reco')
            elif 'can you see me' in message or 'see me' in message or 'tell me my name' in message:
                q.put('speak_reco')
            elif 'can you see this' in message or 'see this' in message or 'tell me what is this' in message or 'detect this' in message:
                print('detection')
                q.put('speak_detect')
          
            elif "tell me about yourself" in message:
                import hello
                hello.intro()
            
            elif "hi robo" in message or "hello robo" in message or "hi robot" in message or "hello robot" in message or "hey robo" in message or "hey robot" in message or "hay robot" in message or "hay robot" in message:
              
                greeting()
            
                elif 'year' in query or ('current' in query and 'year' in query):
                current_date = date.today()
                m = current_date.year
                print(f'Current year is {m}')
                robo_tts.talk_gtts(f'Current year is {m}')
                
            elif "robo move" in message or "robot move" in message or "start autopilot" in message or "autopilot" in message:
                #move_ar = move_ret(1)  
                t2.start()
            elif "robo stop move" in message or "robt stop move"in message or "stop"in message:
                q.put('stop')
            elif "stop code" in message:
                q.put("END")
                break
                '''elif 'image' in query:
                path = "C:\Program Files\Internet Explorer\images"
                os.startfile(path)'''
            else:
                mess = assistant.request(message)
                #print(mess)
                
                if "google" in mess:
                    query = message
                    google_sdk()
                
                elif "trc face" in mess:
                    q.put('face_trc')
                    name = q.get()
                    print(name)
                elif "trc color" in mess:
                    # trc color
                    q.put('color_trc')

                    
                else:
                    talk_gtts(mess, 'en')
            

       


        
        except:
            print('listen...')
            pass
       
    print("close All connection")
    #sys.exit()

   
    
   
    

 
