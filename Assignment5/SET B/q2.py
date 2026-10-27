from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def feedback():
    name =""
    rating = ""
    comments = ""
    if request.method=="POST":
        name=request.form["name"]
        rating=request.form["rating"]
        comments=request.form["comments"]
    return render_template("q2.html",name=name,rating=rating,comments=comments)
app.run(debug=True)