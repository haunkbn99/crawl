import json       
f = open('data.json')
data = json.load(f)
data = data[0]
print(data)
data1 = {}
for token in data:
    data1[token] = []
    data1[token].append(data[token])
with open('data.json', 'w') as outfile:
    json.dump(data1, outfile)