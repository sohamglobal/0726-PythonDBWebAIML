from flask import Flask,request
import pymysql
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/account/new",methods=['POST'])
def add_account():
    ano=int(request.form.get("accno"))
    anm=request.form.get("accnm")
    typ=request.form.get("acctype")
    bal=float(request.form.get("balance"))
    dic={}
    try:
        connection=pymysql.connect(
            host='mysql-py0726-praffull-py0726.a.aivencloud.com',
            port=19972,
            user='avnadmin',
            password='AVNS_pgl8dVT3nsi5MndPaFY',
            database='defaultdb',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor=connection.cursor()
        cursor.execute(f"insert into accounts values({ano},'{anm}','{typ}',{bal})")
        connection.commit()
        connection.close()
        dic['status']='success'
    except:
        dic['status']='failed'

    return dic

app.run(debug=True)
