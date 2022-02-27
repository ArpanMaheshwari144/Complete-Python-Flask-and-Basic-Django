from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

# Program app.run() ki madad se run hoga
@app.route('/about')
def arpan():
    name="Adarsh"
    return render_template('about.html',name1=name)

app.run(debug=True)   # debug=True means agar koi change hoga program mei to wo bina dobara reload kare reflect hoga