'''
Form to JSON Parser
'''

import tkinter as tk
import tkinter.messagebox as mb
import json
import re

# true email validation probably not going to happen
# but this at least checks the domain for basic stuff
# decided not to use it and instead use dumb regex 
#from validate_email import validate_email

# general appearances
opts1 = { 'ipadx': 5, 'ipady': 5 , 'sticky': 'nswe' } # centered
opts2 = { 'ipadx': 5, 'ipady': 5 , 'sticky': 'e' } # right justified
opts3 = { 'ipadx': 5, 'ipady': 5 , 'sticky': 'w' } # left justified

# other options to play with:
# -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky

bgcolor = '#ECECEC'
white = '#FFFFFF'

class App(tk.Tk):
	def __init__(self):
		super().__init__()

		self.title("Form to JSON Parser")

		# corners for spacing/layout
		self.label_nw = tk.Label(self, text=" ", bg=bgcolor)
		self.label_nw.grid(row=0, column=0, **opts1)
		self.label_ne = tk.Label(self, text=" ", bg=bgcolor)
		self.label_ne.grid(row=0, column=9, **opts1)

		# first header
		self.label_a = tk.Label(self, text="Paste Form Info Below", bg=bgcolor)
		self.label_a.grid(row=0, column=1, columnspan=8, **opts1)
		
		# variables we are using/looking for
		self.name = tk.StringVar()
		self.mail = tk.StringVar()
		self.cell = tk.StringVar()
		self.text = tk.Text(self, width=50, height=10, bg=white)

		# go ahead and focus on the paste to field
		self.text.focus_set()

		# text box placed after defined
		self.text.grid(row=1, column=1, columnspan=8, rowspan=5, **opts1)

		# second header
		self.label_b = tk.Label(self, text="Parse or Save Data as JSON", bg=bgcolor)
		self.label_b.grid(row=7, column=1, columnspan=8, **opts1)
		
		# manual form
		tk.Label(self, text="Name").grid(row=8, column=1, columnspan=3, **opts2)
		tk.Entry(self, textvariable=self.name).grid(row=8, column=4, columnspan=5, **opts3)

		tk.Label(self, text="Email").grid(row=9, column=1, columnspan=3, **opts2)
		tk.Entry(self, textvariable=self.mail).grid(row=9, column=4, columnspan=5, **opts3)

		tk.Label(self, text="Cell Phone").grid(row=10, column=1, columnspan=3, **opts2)
		tk.Entry(self, textvariable=self.cell).grid(row=10, column=4, columnspan=5, **opts3)

		# third header/blank
		self.label_c = tk.Label(self, text=" ", bg=bgcolor)
		self.label_c.grid(row=11, column=1, columnspan=8, **opts1)

		# buttons
		self.btn_clear = tk.Button(self, text="Clear",command=self.clear_text, bg=bgcolor)
		self.btn_clear.grid(row=12,column=1, columnspan=2, **opts1)

		self.btn_parse = tk.Button(self, text="Parse",command=self.parse_text, bg=bgcolor)
		self.btn_parse.grid(row=12,column=3, columnspan=2, **opts1)

		self.btn_print = tk.Button(self, text="Next",command=self.print_selection, bg=bgcolor)
		self.btn_print.grid(row=12,column=5, columnspan=2, **opts1)

		self.btn_save = tk.Button(self, text="Save",command=self.save_selection, bg=bgcolor)
		self.btn_save.grid(row=12, column=7, columnspan=2, **opts1)

		# final header
		self.label_b = tk.Label(self, text=" ", bg=bgcolor)
		self.label_b.grid(row=13, column=1, columnspan=8, **opts1)

	# Functions for buttons
	def clear_text(self):
		# clear out the trash
		self.text.delete("1.0", tk.END)
		self.name.set("")
		self.mail.set("")
		self.cell.set("")

		# load sample data
		sample = '''
Name
John Smith
Email
jsmith@gmail.com
Cell Phone
9725551212
Applying For:
Full Time
'''
		# how to load data into a textarea 
		self.text.insert(tk.INSERT, sample)
		print("Sample data loaded")

	def parse_text(self):
	# parses big block and fills out fields with data we weanted 

		# text widget adds a new line, so check if right before that there is nothing
		# couldn't get this to work either.  todo
		if len(self.text.get("1.0", "end-1c")) == 0:
			mb.showinfo("Information", "No Data to Parse.  Click 'Clear' for Sample Data")
			print("Try clicking 'CLEAR', to get sample data")
		else:
			# load up our data
			data = self.text.get("1.0", tk.END)
			lines = data.split("\n")

			# skip through weird sometimes blank lines
			iter = 0
			for line in lines:
				if (len(line) < 3):
					iter = iter + 1
					continue
				else:
					break

			# ok we think this is the right stuff
			name = lines[iter + 1]
			mail = lines[iter + 3]
			cell = lines[iter + 5]

			self.name.set(name)
			if (len(name) < 5):
				mb.showinfo("Information", "Name seems TOO SHORT.  Verify it")

			# ask the host SMTP if the email exists, but don't send email
			#if not validate_email(mail,verify=False): # kinda does nothing
			#if not validate_email(mail,verify=True):  # adds 2 second delay, not 100% anyway
			if not re.match(r"[^@]+@[^@]+\.[^@]+", mail):  # this one kinda works, but allows some weird
				mb.showinfo("Information", "Email Seems WRONG.  Verify it")			
			else:
				self.mail.set(mail)

			# couldn't get email validaiton or regexes to work! todo
			#self.mail.set(mail)

			# set phone properly though
			phone = re.sub('\D', '', cell) # digits only, erase the rest

			# rebuild number to our spec, assuming it's right
			# will error here if it's wrong on CLI and later via gui
			# index out of bounds if it's too short, didn't want to error check 2x
			a = phone[0:3]
			b = phone[3:6]
			c = phone[6:10]

			# assume it's right, rebuild
			rebuilt = a + "-" + b + "-" + c
			
			# now see if it still is likely a phone number or not
			if (len(phone) == 10):
				print(rebuilt + ": parse successful")
			else:
				mb.showinfo("Information", "Phone numer (" + rebuilt + ") is WRONG for some reason, verify it")

			# it's probably right, or you've been warned at least
			self.cell.set(rebuilt)

	def print_selection(self):
	# dumps selection under mouse, or defaults to form fields  to screen
	# put in place for error checking, not really needed for any function
	# kept for demonsttraion purposes
		selection = self.text.tag_ranges(tk.SEL)

		# IF you have something selected
		if selection:
			content = self.text.get(*selection)
			print(content)
		# ELSE just print the parse
		else:
			content = self.name.get() + "\n" + self.mail.get() + "\n" + self.cell.get()
			print(content)

	def save_selection(self):
	# dumps captured data to json file

		# if error detected, flag will set to 0
		flag = 1
		name = self.name.get()
		mail = self.mail.get()
		cell = self.cell.get()

		if (len(name) < 3):
			mb.showinfo("Information", "Name Field Empty?")
			flag = 0
		if (len(mail) < 3):
			mb.showinfo("Information", "Mail Field Empty?")
			flag = 0
		if (len(cell) < 3):
			mb.showinfo("Information", "Cell Field Empty?")
			flag = 0

		if (flag == 1):
			data = {
				"name": self.name.get(),
				"mail": self.mail.get(),
				"cell": self.cell.get()
			}

			# build our json file name
			file = self.cell.get() + ".json"

			# dump to json, clobber existing file of same name
			with open(file, 'w') as outfile:
				json.dump(data, outfile)

			# explain to user what happened
			print(file + " updated")
		else:
			# or don't
			mb.showinfo("Information", "FILE NOT SAVED, FIELDS MIGHT BE EMPTY")

# ok, do the stuff above
if __name__ == "__main__":
	app = App()
	app.mainloop()