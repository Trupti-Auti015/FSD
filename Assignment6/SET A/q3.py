from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    names=["Trupti","Sai","Anushka","Gauravi","Tanishka"]
    names.sort()
    return render_template("q3.html",names=names)
app.run(debug=True)