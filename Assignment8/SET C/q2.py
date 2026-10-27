
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Vehicle")
    cur.execute("""
        CREATE TABLE Vehicle(
            id INT PRIMARY KEY,
            name VARCHAR(50),
            price INT
        )
    """)
    cur.execute("""
        INSERT INTO Vehicle VALUES
        (1, 'Car', 500000),
        (2, 'Bike', 100000),
        (3, 'Bus', 800000),
        (4, 'Truck', 900000),
        (5, 'Scooter', 80000)
    """)
    cur.execute("UPDATE Vehicle SET price = 600000 WHERE id = 1")
    cur.execute("DELETE FROM Vehicle WHERE id = 5")
    conn.commit()

    cur.execute("SELECT * FROM Vehicle")
    data = cur.fetchall()

    cur.close()
    conn.close()
    return str(data)

if __name__ == "__main__":
    app.run(debug=True)
