
import psycopg2
import psycopg2.extras
from flask import Flask, render_template,request,redirect



app =Flask(__name__)


@app.route('/')
def intex():
    return render_template("home.html")



@app.route("/product")
def product():
    return render_template("product.html")
@app.route("/header")
def header():
    return render_template("header.html")

def dbcon():
    connectionString='dbname=asset user=postgres password=sak123 host=localhost'

    try:
        con= psycopg2.connect('database= asset user= postgres password= postgre host= localhost')
        return con
    except:
        print('can not connect')

@app.route("/productGroup")
def productGroup():
    conn=dbcon()
    cur=conn.corsor()
    cur.execute('select * from asset')
    result=cur.fetchall()
    print(result)

    try:
        cur.execute("select * from productgroup")
    except:
        print ("can not excecute")
    result = cur.fetchall()
    print (result)
    return render_template("productGroup.html")

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5000, debug=True)
