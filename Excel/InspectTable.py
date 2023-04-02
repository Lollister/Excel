
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="lorenz",
  database="mydatabase"
)

mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM democrats")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)