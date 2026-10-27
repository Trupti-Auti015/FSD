from flask import Flask , request ,jsonify 

app =Flask(__name__)

students=[
        {"name":"Trupti","marks": 90, "result":"Pass"},
        {"name":"Gauravi","marks": 90, "result":"Pass"},
]
@app.route("/result",methods=["GET"])
def get_result():
    return jsonify(students)

@app.route("/result",methods=["POST"])
def add_result():
    data = request.get_json()
    name = data.get("name")
    marks= data.get("marks")
    
    if marks>=40:
        result="Pass"
    else:
        result ="Fail"
    
    student={"name":name ,"marks":marks ,"result":result}
    students.append(student)
    return jsonify(student)

if __name__=='__main__':
    app.run(debug=True)
    