import string
from flask import Flask,request,redirect,render_template




app = Flask(__name__)
app.config['DEBUG'] = True

def valid_username(username):
    if ' ' in username or len(username) == 0 or len(username)<3 or len(username)>20:
        return False
    return True   

def valid_password(password):
    if password.find(' ') != -1 or len(password) == 0 or len(password)<3 or len(password)>20:
        return False
    return True   
def valid_email(email):
    if email:
        if  email.find(' ') != -1 or len(email)<3 or len(email)>20 or email.count('@') > 1 or email.count('@') < 1 or  email.count('.') >1 or email.count('.') <1:
            return False
    return True
      
@app.route('/signup',methods=['GET','POST'])
def signup():

    if request.method=='GET':
        return render_template('signup.html') 

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        if  valid_username(username) and valid_password(password) and valid_email(email) and (password==verify):
            return redirect('/welcome?username='+username)
        else:
            if not valid_username(username):
                username_error = "That is not a valid username"
            else:
                username_error = ""
            if not valid_password(password):
                password_error= "That is not a valid password"    
            else:
                password_error =""
            if not password == verify  :
                verify_password_error = "passwords dont match"
            else:
                verify_password_error = ""    
            if not valid_email(email):
                email_error = "Not a valid email"
            else:
                email_error = ""    

            return render_template('signup.html',username_error = username_error,
                                                        password_error=password_error,
                                                        verify_password_error=verify_password_error,
                                                        email_error=email_error,username=username,email=email
                                                        ) 
@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html',username =username)
  
app.run()
