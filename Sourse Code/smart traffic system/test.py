import mysql.connector
import sys
try:
    Codebreak = mysql.connector.connect(host="Kshitija04.mysql.pythonanywhere-services.com", user="Kshitija04", passwd="Bugbusters@123", database="Kshitija04$Codebreak")
except:
    sys.exit("Error connecting to the database. Please check your inputs.")
print(Codebreak)