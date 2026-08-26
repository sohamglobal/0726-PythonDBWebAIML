import csv

with open("students.csv","r") as file:
    data=csv.reader(file)
    for record in data:
        print(record)