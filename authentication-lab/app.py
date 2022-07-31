from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

	# // Import the functions you need from the SDKs you need

# // TODO: Add SDKs for Firebase products that you want to use
# // https://firebase.google.com/docs/web/setup#available-libraries

# // Your web app's Firebase configuration
# // For Firebase JS SDK v7.20.0 and later, measurementId is optional
firebaseConfig = {
  "apiKey": "AIzaSyAQoLPIPjHtK95Jr1v3-eowa-8BzLpeMQI",
  "authDomain": "farid-ad80f.firebaseapp.com",
  "projectId": "farid-ad80f",
  "storageBucket": "farid-ad80f.appspot.com",
  "messagingSenderId": "419774116955",
  "appId": "1:419774116955:web:e59e90d48a579e2625bb7e",
  "measurementId": "G-N026B926XY",
  "databaseURL" : ""
}

# // Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

																																																																																																																																																														
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
	 error = ""
	 if request.method == 'POST':
	 	email = request.form['email']
	 	password = request.form['password']
	 	try:
	 		login_session['user'] = auth.sign_in_with_email_and_password(email, password)
	 		return redirect(url_for('add_tweet'))
	 	except:
	 		error = "Authentication failed"
	 return render_template("signin.html")

    


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	 error = ""
	 if request.method == 'POST':
	 	email = request.form['email']
	 	password = request.form['password']
	 	try:
	 		login_session['user'] = auth.create_user_with_email_and_password(email, password)
	 		return redirect(url_for('add_tweet'))
	 	except:
	 		error = "Authentication failed"
	 return render_template("signup.html")
    


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")






if __name__ == '__main__':
    app.run(debug=True)