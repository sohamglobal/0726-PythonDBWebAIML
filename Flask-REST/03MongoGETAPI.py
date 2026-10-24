from flask import Flask,jsonify
from pymongo import MongoClient


app=Flask(__name__)


client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.luhfnai.mongodb.net/?appName=sharayucluster")
db=client['spiderdb']
coll=db['applicants']

@app.route('/applicants',methods=['GET'])
def getapplicants():
    data=list(coll.find())
    return jsonify(data)

app.run(debug=True)