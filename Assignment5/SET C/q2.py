from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    name=""
    quantity=""
    price =""
    if request.method=="POST":
        name=request.form["name"]
        quantity=request.form["quantity"]
        price=request.form["price"]
    return render_template("q2.html",name=name,quantity=quantity,price=price)
app.run(debug=True)