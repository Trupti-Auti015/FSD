from flask import Flask,render_template,request

app= Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    area= ""
    
    if request.method=="POST":
        length= int(request.form["length"])
        breath=int(request.form["breath"])
        area =length * breath
    
    return render_template("q3.html",area=area)

app.run(debug=True)
