import json

def flatten(d,i,j):
 if d:
  if d.get(i):
   if d[i].get(j):
    value = ''
    for string in d[i][j]:
     value += string + '|'
    return value[:-1]
 return ''

def fix(string):
  para = 0;
  for i in range(len(string)):
    if string[i] == '(':
      para += 1
    elif string[i] == ')':
      para -= 1
    elif string[i] == '|' and para == 0:
      return '('+string+')'
  return string

def fix2(string):
  if string == '' or string == '$':
    return ''
  if len(string) == 1:
    return string+'*'
  return '('+string+')*'

data = []
with open(raw_input('Enter file name: ')) as f:
  data = json.load(f)

states = data['states']
states.append(0)
states.append(-1)

transitions = {}
for first in states:
  transitions[first] = {}
  for second in states:
    transitions[first][second] = flatten(data['transitions'],first,second)

transitions[0][data['start']] = '$'

for end in data['accept']:
  transitions[end][-1] = '$'

for i in range(len(states)-2):
  state = states[i]
  for first in states[i+1:]:
    if transitions[first][state] == '':
      continue
    for second in states[i+1:]:
      if transitions[state][second] == '':
        continue
      old = fix(transitions[first][second])
      beg = fix(transitions[first][state])
      mid = fix2(transitions[state][state])
      end = fix(transitions[state][second])
      temp = ''
      if old != '':
        temp = old+'|'
      temp += beg
      temp += mid
      temp += end
      transitions[first][second] = temp

print transitions[0][-1]
