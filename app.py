from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'  # Use '127.0.0.1' if needed
app.config['MYSQL_USER'] = 'joan'
app.config['MYSQL_PASSWORD'] = 'whatthehealth'
app.config['MYSQL_DB'] = 'healthcare_db'
app.config['DEBUG'] = False  # Disable debug to prevent hanging

mysql = MySQL(app)

@app.route('/api/data')
def get_data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM healthcare_bills")
    data = cur.fetchall()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Allow Codespaces access
