from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    name=""
    if request.method=="POST":
        name= request.form["name"]
    return render_template("studentname.html",name=name)
app.run(debug=True) 