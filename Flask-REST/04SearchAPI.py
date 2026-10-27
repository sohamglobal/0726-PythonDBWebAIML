from flask import Flask,jsonify
import pymysql
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/accounts/search/<ano>",methods=['GET'])
def search_account(ano):
    connection=pymysql.connect(
        host='mysql-py0726-praffull-py0726.a.aivencloud.com',
        port=19972,
        user='avnadmin',
        password='AVNS_pgl8dVT3nsi5MndPaFY',
        database='defaultdb',
        cursorclass=pymysql.cursors.DictCursor
        )
    cursor=connection.cursor()
    cursor.execute(f"select * from accounts where accno={ano}")
    data=cursor.fetchone()
    connection.close()
    return jsonify(data)

@app.route('/accounts/type/<typ>',methods=['GET'])
def search_type(typ):
    connection=pymysql.connect(
        host='mysql-py0726-praffull-py0726.a.aivencloud.com',
        port=19972,
        user='avnadmin',
        password='AVNS_pgl8dVT3nsi5MndPaFY',
        database='defaultdb',
        cursorclass=pymysql.cursors.DictCursor
        )
    cursor=connection.cursor()
    cursor.execute(f"select * from accounts where acctype='{typ}'")
    data=cursor.fetchall()
    connection.close()
    return jsonify(data)

app.run(debug=True)