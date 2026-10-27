from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("loginform.html")
   
@app.route("/login",methods=["POST"])
def login():
    username=request.form["username"]
    password=request.form["password"]
    
    if  username=="admin"  and password=="1234":
        return "Login Successful"
    else:
        return "invalid username or password"
app.run(debug=True)
    