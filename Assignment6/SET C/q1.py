from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def employee():
    employees=[
        {"name":"Trupti","salary":5000000},
        {"name":"Sai","salary":300000},
        {"name":"Tanishka","salary":400000}
        
    ]
    return render_template("q1.html",employees=employees)
app.run(debug=True)