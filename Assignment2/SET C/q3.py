from flask import Flask , render_template,request   
app= Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    result=""
    if request.method=="POST":
        name=request.form["name"]
        result="search result:" +name
    return render_template("library.html",result=result)
app.run(debug=True)   
    