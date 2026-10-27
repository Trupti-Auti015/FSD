from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    marks = [70, 80, 60, 90, 75]

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return render_template("q3.html",
    marks=marks, total=total, average=average, highest=highest, lowest=lowest)

app.run(debug=True)