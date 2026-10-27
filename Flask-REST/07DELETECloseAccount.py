from flask import Flask,request
import pymysql
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/account/close",methods=['DELETE'])
def deposit():
    ano=int(request.form.get("accno"))
    
    connection=pymysql.connect(
            host='mysql-py0726-praffull-py0726.a.aivencloud.com',
            port=19972,
            user='avnadmin',
            password='AVNS_pgl8dVT3nsi5MndPaFY',
            database='defaultdb',
            cursorclass=pymysql.cursors.DictCursor
    )
    cursor=connection.cursor()
    cursor.execute(f"delete from accounts where accno={ano}")
    connection.commit()
    connection.close()
    dic={'status':'success'}
    return dic


app.run(debug=True)