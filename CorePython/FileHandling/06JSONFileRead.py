import json

file=open("user.json","r")

data=json.load(file)
print(data)
file.close()