from flask import Flask ,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login" , methods=["POST"])
def login():
    username=request.form["username"]
    password=request.form["password"]
    
    return "Login Successful"
app.run(debug=True)