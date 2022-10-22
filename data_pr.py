import json 
with open('/media/password/nvidia/robo_AI/data.json', 'r') as f:
    json_obj = json.loads(f.read())
print(json_obj['emp4'])
print(json_obj['emp4']['patterns'].append('ho'))