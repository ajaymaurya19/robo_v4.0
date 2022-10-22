# Python program to convert text
# file to JSON

import datetime
import json

time = datetime.datetime.now().strftime('%I:%M%p')


# the file to be converted
filename = "/media/robo/nvidia/Robo 3.0/semples.txt"

# resultant dictionary
dict1 = {}

l =0

with open(filename) as fh:
	
	f1 = fh.readlines()
	f1 = [s.rstrip('\n') for s in f1]
	l =0
	y = ''
	for x in f1:
		dict2 = {}
		print(x)
		l =1
	    
		sno ='emp'+str(l)
		y = 'no' #input('Answer: ')
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
out_file = open(f"/media/robo/nvidia/database/data.json", "w")		
		#out_file = open(f"/media/password/nvidia/robo_AI/data_{time}.json", "w")
json.dump(dictionary, out_file, indent = 4)
out_file.close()
