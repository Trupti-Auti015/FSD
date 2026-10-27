from flask import Flask

app=Flask(__name__)

@app.route("/student/<name>")
def student(name):
    return "Welcome" + name
app.run(debug=True)