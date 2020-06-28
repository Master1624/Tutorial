from flask import Flask
from flask_mysqldb import MySQL
from tutoriales import secret

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:9000'
app.config['SECRET_KEY'] = '40123800b6ec8ae581f4aadf7e40837b'

app.config['MYSQL_HOST'] = secret.dbhost
app.config['MYSQL_USER'] = secret.dbuser
app.config['MYSQL_PASSWORD'] = secret.dbpassword
app.config['MYSQL_DB'] = secret.dbname

db = MySQL(app)

from tutoriales import routes