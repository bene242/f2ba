import mysql.connector
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("file", help="db config file")
args = parser.parse_args()

mhost = ""
muser = ""
mpassword = ""
mdatabase = ""

if args.file:
    with open(args.file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            #print(row)
            
            mhost = row['host']
            muser = row['user']
            mpassword = row['password']
            mdatabase = row['database']
            if True:
                break

mydb = mysql.connector.connect(
    host=mhost,
    user=muser,
    password=mpassword,
    database=mdatabase
)
print(mydb)
