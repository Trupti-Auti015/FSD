from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    employees=[
        {"name":"Trupti","salary":1000000},
        {"name":"Sai","salary":5000000},
        {"name":"Pooja","salary":10000},
        {"name":"Gauravi","salary":1000000},
        {"name":"Vaishavi","salary":250000},
    ]
    return render_template("q2.html",employees=employees)
app.run(debug=True)