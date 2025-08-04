import os
from flask import Flask
from flask_mysqldb import MySQL     # For newer versions of flask-mysql 
# from flask.ext.mysql import MySQL   # For older versions of flask-mysql
app = Flask(__name__)

mysql = MySQL()

mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or  'localhost'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'db_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Passw0rd'
app.config['MYSQL_DATABASE_DB'] = 'employee_db'
app.config['MYSQL_DATABASE_HOST'] = mysql_database_host
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
    with app.app_context():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        row = cursor.fetchone()
        while row is not None:
        result.append(row[0])
        row = cursor.fetchone()
return ",".join(result)

if __name__ == "__main__":
    app.run()
