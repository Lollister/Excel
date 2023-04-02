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

mycursor.execute("CREATE TABLE democrats (id INT AUTO_INCREMENT PRIMARY KEY, candidate VARCHAR(255), gender VARCHAR(255), race1 VARCHAR(255), race2 VARCHAR(255), race3 VARCHAR(255))")

mycursor.execute("CREATE TABLE demincumbent (id INT AUTO_INCREMENT PRIMARY KEY, incumbent VARCHAR(255), incumbentchallenger VARCHAR(255))")

mycursor.execute("CREATE TABLE demstate (id INT AUTO_INCREMENT PRIMARY KEY, state VARCHAR(255), primarydate VARCHAR(255))")

mycursor.execute("CREATE TABLE demposition (id INT AUTO_INCREMENT PRIMARY KEY, office VARCHAR(255), district VARCHAR(255))")

mycursor.execute("CREATE TABLE demprimary (id INT AUTO_INCREMENT PRIMARY KEY, primaryvotes INT(255), primaryper VARCHAR(255), primaryoutcome VARCHAR(255))")

mycursor.execute("CREATE TABLE demrunoff (id INT AUTO_INCREMENT PRIMARY KEY, office VARCHAR(255), district VARCHAR(255))")

mycursor.execute("CREATE TABLE demendorsement (id INT AUTO_INCREMENT PRIMARY KEY, emilyslist VARCHAR(255), justicedems VARCHAR(255), indivisible VARCHAR(255), pccc VARCHAR(255), ourrevolution VARCHAR(255), sunrise VARCHAR(255), sanders VARCHAR(255), aoc VARCHAR(255), partycommittee VARCHAR(255))")