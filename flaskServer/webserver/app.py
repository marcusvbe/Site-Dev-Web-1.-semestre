from flask import Flask, render_template, request

# imports MySQL module from the Flask-MySQLdb package, 
# to connect Flask applications to MySQL databases.
from flask_mysqldb import MySQL

# import mysql.connector

app = Flask("__name__")
# sets up the configuration for a MySQL database connection 
# in a Flask application.
app.config['MYSQL_HOST'] = 'mysql' # HOST: nome do CONTAINER do MYSQL
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'desafio4'
app.config['MYSQL_PORT'] = 3306
# app.config['MYSQL_UNIX_SOCKET'] = '/var/run/mysqld/mysqld.sock'  # Update the socket file location

# initializes a connection to a MySQL database using the MySQL 
# module and the app object.
mysql = MySQL(app)

@app.route('/') # criando rotas com decorator
def index():
    return render_template("index.html")

@app.route("/quemsomos.html")
def quem_somos():
    return render_template("quemsomos.html")


@app.route('/contato.html', methods=['GET', 'POST'])
def contato():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        cur = mysql.connection.cursor() # abre a conexão
        cur.execute("INSERT INTO contatos(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao)) # %s -> strings
       
        mysql.connection.commit()
    
        cur.close()

        return 'sucesso'
    return render_template('contato.html')
# até aqui foi a inserção dos dados no banco


# rota usuários para listar todos os usuário no banco de dados.
@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contatos")

    if users > 0:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails=userDetails)

if __name__== "__main__":
    app.run(host='0.0.0.0', port=5000)
