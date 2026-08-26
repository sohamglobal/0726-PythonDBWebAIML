import json

data={
    "userid":"ethanhunt",
    "name":"praffull",
    "password":"chelsea786",
    "type":"admin"
}

with open("user.json","w") as file:
    json.dump(data,file,indent=5)

print('JSON file write successful')