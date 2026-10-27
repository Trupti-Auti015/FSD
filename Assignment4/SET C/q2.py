from flask import Flask

app=Flask(__name__)

@app.route("/employee/<name>")
def employee(name):
    return "Hello"   +  name  +  "Welcome to Employee Page"
app.run(debug=True)