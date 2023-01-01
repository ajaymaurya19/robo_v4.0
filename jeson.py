
import json 

intents = json.loads(open("intents.json").read())

for intent in intents['intents']:
     
    print(f"tag {intent['tag']}")
    for pattern in intent['patterns']:
            print(f'Pattern {pattern}')
    for pattern in intent['responses']:
            print(f'Responses {pattern}')
    break
    
