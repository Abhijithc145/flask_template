from flask import Flask,render_template
from form import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']="Asdfghjkl@123"

@app.route('/reg')
def registration():
    form = RegistrationForm()
    return render_template('signup.html',title='Register',form=form)

@app.route('/')
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)


if __name__=='__main__':
    app.run(debug=True)       # It is used to flask run to convert python3 <--file_name-->