import sys
import flask
import psycopg2
app = flask.Flask(__name__)


@app.route('/register', methods=['POST'])
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

    insert_query = "INSERT INTO user(first_name, last_name, mobile_no, username, password) VALUES (%s, %s, %s, MD5(%s))"
    insert_values = (firstname, lastname, mobileno, username, password)
    try:
        db_cursor.execute(insert_query, insert_values)
        chat_db.commit()
        return "success"
    except Exception as e:
        print("Error while inserting the new record :", repr(e))
        return "failure"

@app.route('/login', methods=['POST'])
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


@app.route('/location', methods=['POST'])
def location(msg_received):
    longitude = msg_received["log"]
    latitude = msg_received["lat"]
    description = msg_received["descp"]
    username = msg_received["username"]

    insert_query = "INSERT INTO location (user, longitude, latitude, description) VALUES (%s, %s, %s, MD5(%s))"
    insert_values = (username, longitude, latitude, description)
    try:
        db_cursor.execute(insert_query, insert_values)
        chat_db.commit()
        return "success"
    except Exception as e:
        print("Error while inserting the new record :", repr(e))
        return "failure"

try:
    chat_db = psycopg2.connect(host="ec2-3-220-193-133.compute-1.amazonaws.com",database="d1c1c2jkicje",user="tcykfsyhowqcje",password="1bc7dcbd9c0e7c7f74d3d3d1ed6045c9832048c53bb726e5b9fb26aaf676989c",port="5432")
except:
    sys.exit("Error connecting to the database. Please check your inputs.")
db_cursor = chat_db.cursor()

@app.route('/mode', methods=['GET'])
def low():
    return "Status:LOW"

def medium():
    return "Status:MEDIUM"

def high():
    return "Status:HIGH"