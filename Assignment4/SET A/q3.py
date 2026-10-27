from flask import Flask

app = Flask(__name__)

@app.route("/course/<name>")
def course(name):
    return "Course: " + name
app.run(debug=True)