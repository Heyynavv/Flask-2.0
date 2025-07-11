# #what is flask?
# # - a micro web framework for Python  
# # - it is a popular choice for web development due to its simplicity and extensibility
# # - Flask is built on Werkzeug and Jinja2, which are both excellent web frameworks in their own right


# from flask import *

# app = Flask(__name__) #main/root

# @app.route('/') #a route to the root URL
# def home():

#     return 'This is the home page & I have created a Flask application!'

# @app.route('/about') #a route to the about URL
# def about():
#     return 'This is the about page!'


# @app.route ('/contact') #a route to the contact URL
# def contact():
#     return 'This is the contact page!'


# # routes should be unique
# #routes name should be redeable and descriptive
# #always pass return value in the function as it is seen by the user in the window

# #GET & POST Ddiffernces:
# # - GET: used to retrieve data from the server (read-only) // I need some data
# # - POST: used to send data to the server (create, update, delete) // i need to send some data & process it

# @app.route('/submit' , methods=["GET" , "POST"])
# def submit():
#     if request.method=="POST":
#         return "You send data"
#     else:
#         return "You are just viewing this page"



# --------------------------Creating a login page ------
from flask import *

app = Flask(__name__)
app.secret_key = "supersecret" #use to lock the session 


@app.route('/' , methods=["GET" , "POST"])
def login():
    if request.method =="POST":
        username = request.form.get("username")  #reading data
        password = request.form.get("password")

        if username =="admin" and password =="123":
            session["user"] = username #storing data in session
            return  redirect(url_for("Welcome")) 
        else:
            return Response ("In valid credentials . Try again" , minetype = "text/plain") # by default text/HTML
        
    return """
            <h2> Login page </h>
            <form method="POST">
            Username : <input type ="text" name = "username"><br>
            Password : <input type ="text" name = "password"><br>
            </form>
            <input type="submit" value = "login">

"""

@app.route('/welcome')
def welcome():
    if "user" in session :
        return f'''
        <h2> Welcome , {session["user"]} !
        <a hred = {url_for("logout")}>logout </a>



'''
    