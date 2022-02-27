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


@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')


app.run(debug=True)
