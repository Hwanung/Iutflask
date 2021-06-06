import sqlite3
import csv

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

with open('Iris.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for line in reader:
        print(line)
        if line[0] != 'nom':
            cur.execute("INSERT INTO posts (Id, SepalLengthCm, SepalWidthCm,PetalLengthCm,PetalWidthCm,Species) VALUES (?, ?, ?, ?, ?,?)",
                        (int(line[0]), float(line[1]), float(line[2]),float(line[3]),float(line[4]),str(line[5])))

connection.commit()
connection.close()