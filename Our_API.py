
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'PsyDuck3773.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'PsyDuck3773'
app.config['MYSQL_PASSWORD'] = 'siam0001'
app.config['MYSQL_DB'] = 'PsyDuck3773$Nutrition_Tracker'

mysql = MySQL(app)



@app.route('/')
def hello_world():
    return 'Hello  Flask!'

@app.route('/SearchByName/<string:x>')
def searchByName(x):
    u=f"SELECT * FROM Foods WHERE name ={x};"
    cur = mysql.connection.cursor()
    cur.execute(u)
    data = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]  # Extract column names
    cur.close()

    formatted_data = []
    for row in data:
        formatted_row = {}
        for i in range(len(column_names)):
            formatted_row[column_names[i]] = row[i]
        formatted_data.append(formatted_row)

    return jsonify({"data": formatted_data})




@app.route('/NameList')
def foodname():
    cur = mysql.connection.cursor()
    cur.execute("SELECT name FROM Foods")
    data = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]  # Extract column names
    cur.close()

    formatted_data = []
    for row in data:
        formatted_row = {}
        for i in range(len(column_names)):
            formatted_row[column_names[i]] = row[i]
        formatted_data.append(formatted_row)

    return jsonify({"data": formatted_data})



@app.route('/foodsList')
def foodList():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Foods")
    data = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]  # Extract column names
    cur.close()

    # Convert data to a list of dictionaries
    formatted_data = []
    for row in data:
        formatted_row = {}
        for i in range(len(column_names)):
            formatted_row[column_names[i]] = row[i]
        formatted_data.append(formatted_row)

    return jsonify({"data": formatted_data})



@app.route('/calories')
def calories():
    cur = mysql.connection.cursor()
    cur.execute("SELECT name, calories FROM FoodsNew ORDER BY calories DESC")
    data = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]  # Extract column names
    cur.close()

    # Convert data to a list of dictionaries
    formatted_data = []
    for row in data:
        formatted_row = {}
        for i in range(len(column_names)):
            formatted_row[column_names[i]] = row[i]
        formatted_data.append(formatted_row)

    return jsonify({"data": formatted_data})



@app.route('/Protein')
def Protein():
    cur = mysql.connection.cursor()
    cur.execute("SELECT name, Protein FROM FoodsNew ORDER BY Protein DESC")
    data = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]  # Extract column names
    cur.close()

    # Convert data to a list of dictionaries
    formatted_data = []
    for row in data:
        formatted_row = {}
        for i in range(len(column_names)):
            formatted_row[column_names[i]] = row[i]
        formatted_data.append(formatted_row)

    return jsonify({"data": formatted_data})

@app.route('/Vitamin_A')
def Vitamin_A():
    cur = mysql.connection.cursor()
    cur.execute("SELECT name, Vitamin_A FROM FoodsNew ORDER BY Vitamin_A DESC")
    data = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    cur.close()

    formatted_data = []
    for row in data:
        formatted_row = {}
        for i in range(len(column_names)):
            formatted_row[column_names[i]] = row[i]
        formatted_data.append(formatted_row)

    return jsonify({"data": formatted_data})

@app.route('/Vitamin_C')
def Vitamin_C():
    cur = mysql.connection.cursor()
    cur.execute("SELECT name, Vitamin_C FROM FoodsNew ORDER BY Vitamin_C DESC")
    data = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    cur.close()

    formatted_data = []
    for row in data:
        formatted_row = {}
        for i in range(len(column_names)):
            formatted_row[column_names[i]] = row[i]
        formatted_data.append(formatted_row)

    return jsonify({"data": formatted_data})

@app.route('/Vitamin_D')
def Vitamin_D():
    cur = mysql.connection.cursor()
    cur.execute("SELECT name, Vitamin_D FROM FoodsNew ORDER BY Vitamin_D DESC")
    data = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    cur.close()

    formatted_data = []
    for row in data:
        formatted_row = {}
        for i in range(len(column_names)):
            formatted_row[column_names[i]] = row[i]
        formatted_data.append(formatted_row)

    return jsonify({"data": formatted_data})

@app.route('/Vitamin_E')
def Vitamin_E():
    cur = mysql.connection.cursor()
    cur.execute("SELECT name, Vitamin_E FROM FoodsNew ORDER BY Vitamin_E DESC")
    data = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    cur.close()

    formatted_data = []
    for row in data:
        formatted_row = {}
        for i in range(len(column_names)):
            formatted_row[column_names[i]] = row[i]
        formatted_data.append(formatted_row)

    return jsonify({"data": formatted_data})







