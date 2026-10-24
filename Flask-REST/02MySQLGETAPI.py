from flask import Flask,jsonify
import pymysql
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

# rooturl/players
@app.route('/players',methods=['GET'])
def getplayers():
    connection=pymysql.connect(
        host='mysql-py0726-praffull-py0726.a.aivencloud.com',
        port=19972,
        user='avnadmin',
        password='AVNS_pgl8dVT3nsi5MndPaFY',
        database='defaultdb',
        cursorclass=pymysql.cursors.DictCursor
        )
    cursor=connection.cursor()
    cursor.execute("select * from players")
    data=cursor.fetchall()
    connection.close()
    return jsonify(data)

@app.route('/accounts',methods=['GET'])
def getaccounts():
    connection=pymysql.connect(
        host='mysql-py0726-praffull-py0726.a.aivencloud.com',
        port=19972,
        user='avnadmin',
        password='AVNS_pgl8dVT3nsi5MndPaFY',
        database='defaultdb',
        cursorclass=pymysql.cursors.DictCursor
        )
    cursor=connection.cursor()
    cursor.execute("select * from accounts")
    data=cursor.fetchall()
    connection.close()
    return jsonify(data)

app.run(debug=True)