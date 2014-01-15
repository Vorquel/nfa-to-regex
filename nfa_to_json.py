import json

json_data = ''
with open(raw_input('Enter file name: ')) as f:
  json_data = f.read()
data = json.load(json_data)

states = data['states']
alphabet = data['alphabet']
transitions = data['transitions']

states.append('$start')
transitions['$start'][data['start']] = '_'

states.append('$end')
for end in data['accept']:
  transitions[end]['$end'] = '_'

for i in range(len(states)-2):
  state = states[i]
  for first in states[i+1:]:
    for second in states[i+1:]:
      #todo
