from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Home Page"
@app.route("/about")
def about():
    return "This is about Home Page"
app.run(debug=True)