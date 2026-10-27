from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    total =""
    if request.method=="POST":
        salary=int(request.form["salary"])
        total = salary + 5000
    return render_template("q3.html",total=total)
app.run(debug=True)    
    