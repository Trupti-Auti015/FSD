from flask import Flask
import psycopg2
app = Flask(__name__)

conn = psycopg2.connect(
        dbname="samarth",
        user="postgres",
        password="root",
        host="localhost",
        port="5432")
@app.route('/connect')
def connect_db():
        return "Database Connected Successfully"
@app.route('/create_table')
def create_table():
        try:
                cur = conn.cursor()
                cur.execute("""
                        CREATE TABLE IF NOT EXISTS student (
                                id SERIAL PRIMARY KEY,
                                name VARCHAR(100),
                                age INT,
                                course VARCHAR(50)
                        );""")
                conn.commit()
                cur.close()
                return "Student Table Created Successfully"
        except Exception as e:
                return f"Error: {e}"

# Insert Records
@app.route('/insert')
def insert_students():
        try:
                cur = conn.cursor()
                students = [
                        ('Sai', 24, 'Computer Science'),
                        ('Trupti', 22, 'Information Technology'),
                        ('Pooja', 20, 'Data Science'),
                        ('Gauravi', 23, 'Cyber Security'),
                        ('Arti', 21, 'Artificial Intelligence')
                ]

                cur.executemany(
                "INSERT INTO student (name, age, course) VALUES (%s, %s, %s);",
                students
                )
                conn.commit()
                cur.close()
                return "5 Student Records Inserted Successfully"
        except Exception as e:
                conn.rollback()
        return f"Error: {e}"

if __name__ == "__main__":
        app.run(debug=True)
