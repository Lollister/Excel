import mysql.connector

print("Create DB")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="lorenz"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="lorenz",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE democrats (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), gender VARCHAR(255))")

