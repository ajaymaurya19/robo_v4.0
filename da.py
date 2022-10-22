# Python program to convert text
# file to JSON

import datetime
import json
def write_json(new_data, filename='/media/robo/nvidia/database/data.json'):
	with open(filename,'r+') as file:
		# First we load existing data into a dict.
		file_data = json.load(file)
		# Join new_data with file_data inside emp_details
		file_data["intents"].append(new_data)
		# Sets file's current position at offset.
		file.seek(0)
		# convert back to json.
		json.dump(file_data, file, indent = 4)


time = datetime.datetime.now().strftime('%I:%M%p')


# the file to be converted
filename = "/home/robo/Downloads/dataset.txt"

# resultant dictionary
dict1 = {}

l =0

with open(filename) as fh:
	
	f1 = fh.readlines()
	f1 = [s.rstrip('\n') for s in f1]
	l =0
	q = []
	a = []
	l =89
	#print(f1)
	for x in f1:
		dict2 = {}
		#print(x)
		x = x.split(', ')

	
		if x[0]=='q':
			q.append(x[1])
		
			continue
		elif x[0]=='a':
			a.append(x[1])
		#print(f'{q} \n {a}')
				
						

		
	    
		sno ='emp'+str(l)
		y = 'no' #input('Answer: ')
		dictionary ={
					"tag": sno,
					"patterns": q,
					"responses": a
				
				}
		l = l+1
		#dict1[sno]= dictionary
		print(dictionary)
		q = []
		a = []
		write_json(dictionary)

		# creating json file
'''out_file = open(f"/media/robo/nvidia/database/data.json", "w")		
		#out_file = open(f"/media/password/nvidia/robo_AI/data_{time}.json", "w")
json.dump(dictionary, out_file, indent = 4)
out_file.close()'''
