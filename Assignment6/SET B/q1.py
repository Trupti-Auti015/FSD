from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def studentInfo():
    student={
        "name":"Trupti",
        "age" : 20,
        "course":"BSCIT"
    }
    return render_template("q1.html",student=student)
app.run(debug=True)