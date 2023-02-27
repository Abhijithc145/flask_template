from flask import Flask,render_template
from .form import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']="Asdfghjkl@123"

@app.route('/')
def hello():
    return "home.html"

@app.route('/home')
def home():
    return render_template('home.html')


if __name__=='__main__':
    app.run(debug=True)       # It is used to flask run to convert python3 <--file_name-->