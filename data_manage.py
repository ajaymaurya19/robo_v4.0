from tkinter import *
import json 

intents = json.loads(open("intents.json").read())
def data_json():
    
    for intent in intents['intents']:
        
        print(f"tag {intent['tag']}")
        for pattern in intent['patterns']:
            
                print(f'Pattern {pattern}')
        for pattern in intent['responses']:
                print(f'Responses {pattern}')
        break

all_entries = []

root = Tk()
root.geometry('640x300')
root.title('IoT4Begineers')
frame = Frame(root)


frame.pack()

Label(frame, text='Patterns').grid(row=0, column=0)
Label(frame, text='Respons').grid(row=0, column=1)


pattern_1 = Entry(frame)
pattern_1.grid(row=1, column=0)
pattern_2= Entry(frame)
pattern_2.grid(row=2, column=0)

pattern_3 = Entry(frame)
pattern_3.grid(row=3, column=0)

pattern_4= Entry(frame)
pattern_4.grid(row=4, column=0)

pattern_5= Entry(frame)
pattern_5.grid(row=5, column=0)

pattern_6= Entry(frame)
pattern_6.grid(row=6, column=0)

pattern_7 = Entry(frame)
pattern_7.grid(row=7, column=0)

pattern_8 = Entry(frame)
pattern_8.grid(row=8, column=0)

pattern_9 = Entry(frame)
pattern_9.grid(row=9, column=0)





respons_1= Entry(frame)
respons_1.grid(row=1, column=1)

respons_2 = Entry(frame)
respons_2.grid(row=2, column=1)

respons_3= Entry(frame)
respons_3.grid(row=3, column=1)

respons_4 = Entry(frame)
respons_4.grid(row=4, column=1)

respons_5 = Entry(frame)
respons_5.grid(row=5, column=1)

respons_6 = Entry(frame)
respons_6.grid(row=6, column=1)


respons_7 = Entry(frame)
respons_7.grid(row=7, column=1)

respons_8 = Entry(frame)
respons_8.grid(row=8, column=1)

respons_9 = Entry(frame)
respons_9.grid(row=9, column=1)






submit = Button(frame,text='Submit').grid(row=10, column=1)










root.mainloop()