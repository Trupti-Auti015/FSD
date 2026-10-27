from flask import Flask

app=Flask(__name__)

@app.route("/contact")
def contact():
    return "This is a Contact Page"
@app.route("/services")
def services():
    return "This is Services Page"
app.run(debug=True)