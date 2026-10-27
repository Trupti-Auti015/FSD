from flask import Flask

app= Flask(__name__)

@app.route("/square/<int:num>")
def square(num):
    return "square = " + str(num * num)
app.run(debug=True)
    