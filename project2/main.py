from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')

def index():
    return render_template('home.html')
@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppy.html',name=name)
app.run(debug=True)