from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def StudentMark():
    name="Trupti"
    m1=90
    m2=80
    m3=99
    
    total=m1+m2+m3
    average=total/3
    return render_template("q1.html",
    name=name,m1=m1,m2=m2,m3=m3,total=total,average=average)
app.run(debug=True)