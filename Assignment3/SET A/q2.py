from flask import  Flask 
app= Flask(__name__)

@app.route("/")
def home():
    return "Name:Trupti Auti <br> Roll No:09"
app.run(debug=True)