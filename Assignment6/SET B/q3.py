from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    products=[
        {"name":"Laptop","price":150000},
        {"name":"BMW","price":1000000000},
        {"name":"Owan","price":100000},
    ]
    expensive=products[2]
    return render_template("q3.html",products=expensive)
app.run(debug=True)