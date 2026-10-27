from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    result=""
    if request.method=="POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        result= num1+num2
    return render_template("q2.html",result=result)
app.run(debug=True)
    