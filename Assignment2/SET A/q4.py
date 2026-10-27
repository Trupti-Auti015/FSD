from flask import Flask ,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("feedbackform.html")

@app.route("/feedback",methods=["POST"])
def feedback():
    if request.method == "POST":
        name= request.form["name"]
        feedback=request.form["feedback"]
        
        return "Thank You For Your Feedback,"+name
app.run(debug=True)