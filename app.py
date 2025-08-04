import os
from flask import Flask
from flask_mysqldb import MySQL     # For newer versions of flask-mysql 
# from flask.ext.mysql import MySQL   # For older versions of flask-mysql 
app = Flask(__name__)

mysql = MySQL()

mysql_database_host = os.environ.get('DB_HOST', 'localhost')

# MySQL configurations
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'flaskpass'
app.config['MYSQL_DB'] = 'flaskdb'
app.config['MYSQL_HOST'] = mysql_database_host
mysql.init_app(app)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/read from database')
def read():
    
        result = []
        conn = mysql.connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        row = cursor.fetchone()
        while row is not None:
            result.append(row[0])
            row = cursor.fetchone()
        cursor.close()
        return ",".join(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
