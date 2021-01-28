import sys

import flask
import mysql.connector

app = flask.Flask(__name__)


@app.route('/user', methods=['GET', 'POST'])
def chat():
    msg_received = flask.request.get_json()
    msg_subject = msg_received["subject"]

    if msg_subject == "register":
        return register(msg_received)
    elif msg_subject == "login":
        return login(msg_received)
    else:
        return "Invalid request."


def register(msg_received):
    firstname = msg_received["firstname"]
    lastname = msg_received["lastname"]
    mobileno = msg_received["mobileno"]
    username = msg_received["username"]
    password = msg_received["password"]

    select_query = "SELECT * FROM user where username = " + "'" + username + "'"
    db_cursor.execute(select_query)
    records = db_cursor.fetchall()
    if len(records) != 0:
        return "Another user used the username. Please chose another username."

    insert_query = "INSERT INTO user (first_name, last_name, mobile_no, username, password) VALUES (%s, %s, %s, MD5(%s))"
    insert_values = (firstname, lastname,mobileno, username, password)
    try:
        db_cursor.execute(insert_query, insert_values)
        chat_db.commit()
        return "success"
    except Exception as e:
        print("Error while inserting the new record :", repr(e))
        return "failure"


def login(msg_received):
    username = msg_received["username"]
    password = msg_received["password"]

    select_query = "SELECT first_name, last_name FROM user where username = " + "'" + username + "' and password = " + "MD5('" + password + "')"
    db_cursor.execute(select_query)
    records = db_cursor.fetchall()

    if len(records) == 0:
        return "failure"
    else:
        return "success"


try:
    chat_db = mysql.connector.connect(host="localhost", user="root", passwd="mysql12345", database="traffic")
except:
    sys.exit("Error connecting to the database. Please check your inputs.")
db_cursor = chat_db.cursor()
app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
