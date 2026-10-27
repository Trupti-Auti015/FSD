from flask import Flask

app=Flask(__name__)

@app.route("/product/<int:id>")
def product(id):
    return "Product ID:"  + str(id)
app.run(debug=True)
    