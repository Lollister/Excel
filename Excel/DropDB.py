import mysql.connector

print("Drop DB")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="lorenz",
  database="mydatabase"
)
mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE mydatabase")