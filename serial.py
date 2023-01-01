import serial
import tkinter as tk
import customtkinter
import threading
import queue
import time

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#app = customtkinter.CTk()  # create CTk window like you do with the Tk window
#app.geometry("400x240")
#app.title("Maker Tutor-Python arduino LED controller")

servo_value = 0
txt = "Arduino LED Controller" 



#arduino_ready = True
#arduino = serial.Serial(port = 'COM10', baudrate = 115200, timeout=1)

class SerialThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        s = serial.Serial('COM10',115200, timeout=1)
        
        time.sleep(0.2)
        while True:
            if s.inWaiting():
                text = s.readline(s.inWaiting())
                self.queue.put(text)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("MakerTutor:Python arduino state")
        self.geometry(f"{400}x{300}")
        self.leds = [0,0,0];

        frameLabel = tk.Frame(self, padx=20, pady =20)
        
        self.text = tk.Text(frameLabel, wrap='word', font='TimesNewRoman 37',
                            bg=self.cget('bg'), relief='flat')
        
        # LED 1

        self.button1 = customtkinter.CTkButton(self, text="LED1",fg_color="black" ,command=self.button1_function)
        self.button1.place(relx=0.3, rely=0.3, anchor=tk.CENTER)

        # LED 2

        self.button2 = customtkinter.CTkButton(self, text="LED2",fg_color="black", command=self.button2_function)
        self.button2.place(relx=0.3, rely=0.5, anchor=tk.CENTER)


        # LED 3
        self.button3 = customtkinter.CTkButton(self, text="LED3",fg_color="black", command=self.button3_function)
        self.button3.place(relx=0.3, rely=0.7, anchor=tk.CENTER)

        frameLabel.pack()
        self.text.pack()
        
        self.queue = queue.Queue()
        thread = SerialThread(self.queue)
        thread.start()
        self.process_serial()

    def process_serial(self):
        value=True
        while self.queue.qsize():
            try:
                new=self.queue.get()
                if value:
                    self.text.delete(1.0,'end')
                value=False
                self.text.insert('end',new)
                self.decodeLedState(self.text.get('1.0', tk.END))
                
            except Queue.Empty:
                pass
        self.after(100,self.process_serial)
        
    def button1_function(self):
    
        print("button1 pressed --> LED1 ON")
        self.leds[0] = 1
        #write_data(leds[0],leds[1],leds[2])

    def button2_function(self):
    
        print("button2 pressed --> LED1 OFF")
        self.leds[0] = 0
        #write_data(leds[0],leds[1],leds[2])
    
    def button3_function(self):
    
        print("button3 pressed --> LED2 ON")
        self.leds[1] = 1
        #write_data(leds[0],leds[1],leds[2])    

    def decodeLedState(self,txt):
        
        if ';' in txt:
            ledstate = txt.split(";")
            ledstate[1].replace("\n", "")
            
            print(ledstate[1])
            if int(ledstate[0]) == 1:
                self.button1.configure(fg_color="Yellow")
            else:
                self.button1.configure(fg_color="Black")
                
            if int(ledstate[1]) == 1:
                self.button2.configure(fg_color="Yellow")
            else:
                self.button2.configure(fg_color="Black")    

if __name__ == "__main__":
    app = App()
    app.mainloop() 