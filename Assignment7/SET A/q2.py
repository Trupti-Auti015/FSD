from flask import Flask,request,jsonify

app =Flask(__name__)
 
employee=[
    {"name":"Trupti","department":"IT"},
    {"name":"Sai","department":"HR"}
]
@app.route("/employee",methods=["GET"])
def get_employee_details():
    return jsonify(employee)

@app.route("/employee",methods=["POST"])
def add_employee():
    data = request.get_json()
    employee.append(data)
    return jsonify({"msg":"Employee Added Successfully","employee":data})

if __name__=='__main__':
    app.run(debug=True)

