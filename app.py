from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime, timedelta

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sureshmd515",
    database="maintenance_db"
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT *, DATEDIFF(NOW(), last_maintenance) AS days_passed FROM machines")
    machines = cursor.fetchall()
    return render_template('index.html', machines=machines)

@app.route('/add_machine', methods=['GET', 'POST'])
def add_machine():
    if request.method == 'POST':
        name = request.form['name']
        type_ = request.form['type']
        last_maintenance = request.form['last_maintenance']
        frequency = int(request.form['frequency'])
        cursor.execute("INSERT INTO machines (name, type, last_maintenance, frequency) VALUES (%s, %s, %s, %s)",
                       (name, type_, last_maintenance, frequency))
        db.commit()
        return redirect(url_for('index'))
    return render_template('add_machine.html')

@app.route('/log_maintenance/<int:machine_id>')
def log_maintenance(machine_id):
    today = datetime.now().strftime('%Y-%m-%d')
    cursor.execute("UPDATE machines SET last_maintenance=%s WHERE id=%s", (today, machine_id))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)