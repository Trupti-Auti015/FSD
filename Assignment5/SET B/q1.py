from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def employee():
    name =""
    age = ""
    salary = ""
    if request.method=="POST":
        name=request.form["name"]
        age=request.form["age"]
        salary=request.form["salary"]
    return render_template("q1.html",name=name,age=age,salary=salary)
app.run(debug=True)