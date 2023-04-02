import csv
from os import linesep
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="lorenz",
  database="mydatabase"
)

mycursor = mydb.cursor()

with open('C:\\Users\\Lorenz\\Desktop\\primary-project-2022\\dem_candidates.csv') as csv_file:


    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    line_count = 0
    for row in csv_reader:
        line_count += 1
        sql = "INSERT INTO democrats (name, gender) VALUES (%s, %s)"
        val = (row[0], row[1])
        mycursor.execute(sql, val)
        mydb.commit()

print(f'Processed {line_count} lines.')

mycursor.execute("SELECT * FROM democrats")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)