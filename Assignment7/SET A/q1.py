from flask import Flask,request,jsonify

app=Flask(__name__)

students=[
    {"name":"Trupti","course":"BSCIT"},
    {"name":"Gauravi","course":"BSCIT"}
]

@app.route("/student",methods=['GET'])
def get_student():
    return jsonify(students)

@app.route("/student",methods=['POST'])
def add_student():
    data = request.get_json()
    students.append(data)
    return jsonify({"msg":"Student Added successfully" , "student":data})

if __name__=='__main__':
    app.run(debug=True)