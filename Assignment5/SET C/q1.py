from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def login():
    result =" "
    
    if request.method=="POST":
        username= request.form["username"]
        
        if username== "admin":
            result ="valid username"
        else:
            result="invalid username"
    return render_template("q1.html",result=result)
app.run(debug=True)