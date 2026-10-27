from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        marks = int(request.form["marks"])

        if marks >= 40:
            result = "Pass"
        else:
            result = "Fail"

    return render_template("q4.html", result=result)
app.run(debug=True)