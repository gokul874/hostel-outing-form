from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import ssl

app = Flask(__name__)

# Configure db
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

app.config['MYSQL_HOST'] = 'aws.connect.psdb.cloud'
app.config['MYSQL_USER'] = '69osz44pjrgjcwc9lwhm'
app.config['MYSQL_PASSWORD'] = 'pscale_pw_N5D8YDvG3jzMpgymaUZ7bXkaDcCjGF1WJ22cHkfxbtM'
app.config['MYSQL_DB'] = 'project'
app.config['MYSQL_SSL_KEY'] = 'key.pem'
app.config['MYSQL_SSL_CERT'] = 'cert.pem'
app.config['MYSQL_SSL'] = True

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        studentDetails = request.form
        name = studentDetails['student_name']
        email = studentDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student (student_name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

#if __name__ == '__main__':
#    app.run(debug=True)
