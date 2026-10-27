from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def StudentNames():
    names=["Trupti","Gauravi","Sai","Anushka","Vaishnavi"]
    return render_template("q2.html",names=names)
app.run(debug=True)