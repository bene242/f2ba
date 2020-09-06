import csv

file_name = "employees.csv"

with open(file_name, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['id'] + " " + row['first_name'] + " " + row['last_name'])
        if True:
            break
