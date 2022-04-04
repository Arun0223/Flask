from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')

def home():
    name = "Arun kumar"
    age=22
    address={"H_NO":"2-73",'village':"Seethampeta","Mandal":"Jammikunta","Dist":"Karimnagar","Pin":505475}
    return render_template('basic.html',my_var=name,a=age,A=address)

app.run(port=4000)