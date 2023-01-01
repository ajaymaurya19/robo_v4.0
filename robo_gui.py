import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import time
from tkinter.ttk import Progressbar
from PIL import Image,ImageTk
import cv2
from r_servo import move_auto
import os
import psutil
pid = os.getpid()
python_process = psutil.Process(pid)

###############################################################################
# Parameters and global variables

# Default font size
font_size = -24

# Declare global variables
root = None
dfont = None
frame = None
dtime = None

# Global variable to remember if we are fullscreen or windowed
fullscreen = False

###############################################################################
# Functions

# Toggle fullscreen

def main_frame():
    print("main")
    
   # app.grid_forget()
    frame.pack(fill=tk.BOTH, expand=1)
    app.pack_forget()
    #frame.grid(fill=tk.BOTH, expand=1)
    
def appli():
    frame.pack_forget()
    app.pack(fill=tk.BOTH, expand=1)
def toggle_fullscreen(event=None):

    global root
    global fullscreen

    # Toggle between fullscreen and windowed modes
    fullscreen = not fullscreen
    root.attributes('-fullscreen', fullscreen)
    resize()

# Return to windowed mode
def end_fullscreen(event=None):

    global root
    global fullscreen

    # Turn off fullscreen mode
    fullscreen = False
    root.attributes('-fullscreen', False)
    resize()

# Automatically resize font size based on window size
vid = cv2.VideoCapture(0)
def Video():
    video = Label(root)
    video.pack()
    #Getting video from webcam
    #vid = cv2.VideoCapture(0)
    #Loop which display video on the label
    while(True):
        
        ret, frame = vid.read() #Reads the video
        #Converting the video for Tkinter
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        #Setting the image on the label
        video.config(image=imgtk)
        root.update() #Updates the Tkinter window
vid.release()
cv2.destroyAllWindows()
def resize(event=None):

    global time_dfont
    global button_dfont
    global frame

    # Resize font based on frame height (minimum size of 12)
    # Use negative number for "pixels" instead of "points"
    new_size = -max(12, int((frame.winfo_height() / 2)))
    time_dfont.configure(size=new_size)
    new_size = -max(12, int((frame.winfo_height() / 30)))
    button_dfont.configure(size=new_size)

n=1
def update(): 
    global n
    global photo
    photo = ImageTk.PhotoImage(file=f"face/p{n}.jpg")
    n=n+1
    if n >12:
        n =1
    
    
    bg_lbl=Label(frame,image=photo,bg="black")
    bg_lbl.place(x=0,y=0,width=1366,height=768)
    button_quit = tk.Button(frame, 
                        text="Quit", 
                        font=button_dfont, 
                        command=root.destroy,
                        borderwidth=0,
                        highlightthickness=0, 
                        fg='gray10',
                        bg='black')
    button_quit.place(x=0,y=0,width=100,height=50)
    global login_n
    login_n=Button(frame,image=photoimage7,borderwidth=0,cursor="hand2",command=play)
    login_n.place(x=625,y=625)
    app=Button(frame,text="Apps",font=("times new roman",20),borderwidth=0,bg="black",fg="white",command=appli,activebackground="black",activeforeground="white")
    app.place(x=20,y=50)
    '''memoryUse = python_process.memory_info()[0]/2.**30  # memory use in GB...I think

    cpu_u= tk.Label(frame, text=memoryUse,bg="black",fg="white", font=40 ,activebackground="black",activeforeground="white")
    cpu_u.place(x=100,y=700)
    cpu= tk.Label(frame, text='CPU',bg="black",fg="white", font=40 ,activebackground="black",activeforeground="white")
    cpu.place(x=50,y=700)'''
    
    root.after(2000, update)
    
    
    
    
paused= True
def play():
    global paused,photoimage7
    print("start of function",paused)
    if paused:
        img6=Image.open("data/mic_r.jpeg")
        img6=img6.resize((100,100),Image.ANTIALIAS)
        photoimage7=ImageTk.PhotoImage(img6)
  
        paused=False
        print("mic On",paused)
    else:
        img7=Image.open("data/mic_g.jpeg")
        img7=img7.resize((100,100),Image.ANTIALIAS)
        photoimage7=ImageTk.PhotoImage(img7)

        paused=True
        print("mic off", paused)
    
def main_win():
    frame.pack(fill=tk.BOTH, expand=1)
###############################################################################
# Main script

# Create the main window
root = tk.Tk()

root.title("Robo")

frame = tk.Frame(root, bg='black')
app=tk.Frame(root, bg='black')
# Lay out the main container (expand to fit window)
frame.pack(fill=tk.BOTH, expand=1)
#main_win()

time_dfont = tkFont.Font(family='Courier New', size=font_size)
button_dfont = tkFont.Font(size=font_size)

# Bind F11 to toggle fullscreen and ESC to end fullscreen
root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', end_fullscreen)

# Have the resize() function be called every time the window is resized
root.bind('<Configure>', resize)

# Schedule the poll() function to be called periodically
root.after(20, update)
'''S_name = tk.Label(app, text= "Last Name" , font='Verdana 10 bold')
S_name.place(x=100,y=100)'''
img5=Image.open("data/mic_r.jpeg")
img5=img5.resize((100,100),Image.ANTIALIAS)
photoimage7=ImageTk.PhotoImage(img5)



img1=Image.open("data/images.png")
img1=img1.resize((300,300),Image.ANTIALIAS)
photoimage1=ImageTk.PhotoImage(img1)
singup_bt=Button(app,image=photoimage1,borderwidth=0,cursor="hand2",command=move_auto)
singup_bt.place(x=100,y=50)

img2=Image.open("data/servo.png")
img2=img2.resize((300,300),Image.ANTIALIAS)
photoimage2=ImageTk.PhotoImage(img2)
singup_btn=Button(app,image=photoimage2,borderwidth=0,cursor="hand2",command=move_auto)
singup_btn.place(x=525,y=50)

img3=Image.open("data/speaker.jpg")
img3=img3.resize((300,300),Image.ANTIALIAS)
photoimage3=ImageTk.PhotoImage(img3)
singup_btn=Button(app,image=photoimage3,borderwidth=0,cursor="hand2",command=move_auto)
singup_btn.place(x=975,y=50)

img4=Image.open("data/camare.jpg")
img4=img4.resize((300,300),Image.ANTIALIAS)
photoimage4=ImageTk.PhotoImage(img4)
login_btn=Button(app,image=photoimage4,borderwidth=0,cursor="hand2",command=Video)
login_btn.place(x=100,y=425)

img4=Image.open("data/camare.jpg")
img4=img4.resize((300,300),Image.ANTIALIAS)
photoimage5=ImageTk.PhotoImage(img4)
login_btn=Button(app,image=photoimage5,borderwidth=0,cursor="hand2",command=Video)
login_btn.place(x=525,y=425)

img4=Image.open("data/camare.jpg")
img4=img4.resize((300,300),Image.ANTIALIAS)
photoimage6=ImageTk.PhotoImage(img4)
login_btn=Button(app,image=photoimage6,borderwidth=0,cursor="hand2",command=main_frame)
login_btn.place(x=975,y=425)

# Start in fullscreen mode and run
toggle_fullscreen()
root.mainloop()