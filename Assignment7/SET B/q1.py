from flask import Flask, request , jsonify

app= Flask(__name__)

products=[
    {"name":"Laptop","price":750000,"category":"Electronic"},
    {"name":"Mobile","price":500000,"category":"Electronic"},
]

@app.route("/products",methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/products",methods=["POST"])
def add_products():
    data=request.get_json()
    
    name = data.get("name")
    price =data.get("price")
    category= data.get("category")
    product ={"name": name,"price":price ,"category":category}
    products.append(product)
    
    return jsonify({"msg":"Product added successfully","product":product})

if __name__=='__main__':
    app.run(debug=True)