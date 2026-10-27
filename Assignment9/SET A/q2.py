from flask import Flask , request  ,render_template 
import psycopg2

app=Flask(__name__)
def get_connect():
    conn= psycopg2.connect(
        dbname= 'employeedb',
        user= 'postgres',
        password='root',
        host='localhost',
        port="5432"
    )
    return conn
def create_table():
    conn = get_connect()
    cur=conn.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS Employee
                (Employee_ID SERIAL PRIMARY KEY, 
                Name VARCHAR(100),
                Department VARCHAR(100))""")
    
    conn.commit()
    cur.close()
    conn.close()
    
@app.route('/employee',methods=['GET','POST'])
def student():
    conn = get_connect()
    cur = conn.cursor()
    
    if request.method ==  'POST' :
        Name = request.form.get("name")
        Department = request.form.get("department")
        
        cur.execute("INSERT INTO Employee(name ,department) VALUES(%s,%s)",
                    (Name,Department) )
        conn.commit()
    cur.execute("SELECT * FROM Employee ORDER BY Employee_ID")
    employees = cur.fetchall()    
        
    cur.close()
    conn.close()
        
    return render_template("employee.html",employees=employees)
    
if __name__=='__main__':
    create_table()
    app.run(debug=True)