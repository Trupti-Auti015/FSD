from flask import Flask

app=Flask(__name__)

@app.route("/employe")
def employe():
    return "Employe Page"
@app.route("/department")
def department():
    return "Department Page"
@app.route("/contact")
def contact():
    return "Contact Page"
app.run(debug=True)