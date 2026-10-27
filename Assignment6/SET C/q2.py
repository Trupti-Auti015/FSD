from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def studentMark():
    students=[
        {"name":"Trupti","marks":90},
        {"name":"Sai","marks":40},
        {"name":"Gauravi","marks":80}
    ]
    return render_template("q2.html",students=students)
app.run(debug=True)
