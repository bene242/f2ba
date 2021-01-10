#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os.path
import operator
import sqlite3
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="file to work with, format: \
-> 2020-05-24 07:00:30,482 fail2ban.actions        [407]: NOTICE  [sshd] Ban 220.158.148.132 <- \
(raw fail2ban-log)")
parser.add_argument("-d", "--descending", help="sort descending", action="store_true")
parser.add_argument("-c", "--csv", help="output csv", action="store_true")
args = parser.parse_args()

fname =""
fdict = {"0.0.0.0": 0}
hashDate = {"2020-00-00": 0}
#arrayDate[0] = "2020-00-00"


###############################################################################
###############################################################################
def main():
    """ Main program """
    global fname, fdict, hashDate
    regex = re.compile("Ban")
    #check if only 1 Argument
    if args.file:
        fname = args.file
        if (os.path.isfile(fname) != True):
            nofile(fname)

    #parse and save date and ip
    with open(fname) as f:
        for line in f:
            line = line.rstrip()
            result = regex.search(line)
            if result:
                arrg = line.split()
                fdate = arrg[0]
                fip = arrg[7]
                #nach IP
                if fip in fdict:
                    fdict[fip] = fdict[fip]+1
                else:
                    fdict[fip] = 1
                #nach Datum
                if fdate in hashDate:
                    hashDate[fdate] += 1
                else:
                    hashDate[fdate] = 1
        f.close()

        conn = sqlite3.connect(':memory:')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()


        ### save in sqlite3
        save_in_sqlite(cur,conn)

        if args.csv:
            print_csv_from_sqlite(cur)
        else:
            print_from_sqlite(cur)
            print_total_sqlite(cur)
    #    print_ips()

        cur.close()
        conn.close()



###############################################################################
def save_in_sqlite(cur,conn):

    cur.execute("""
        CREATE TABLE IF NOT EXISTS ipees (
            id INTEGER PRIMARY KEY,
            ip TEXT NOT NULL,
            count INTEGER DEFAULT 0
        )
    """)


    for mkeys in fdict:
        anzahl_ips = fdict[mkeys]
        cur.execute("insert into ipees (ip,count) values (?, ?)", (mkeys, anzahl_ips))
        conn.commit()


###############################################################################
def print_from_sqlite(cur):
    if args.descending:
        for row in cur.execute("SELECT ip,count FROM ipees ORDER BY count desc"):
            print(row["ip"], " - ", row["count"])
    else:
        for row in cur.execute("SELECT ip,count FROM ipees ORDER BY count"):
            print(row["ip"], " - ", row["count"])

###############################################################################
def print_csv_from_sqlite(cur):

    if args.descending:
        for row in cur.execute("SELECT ip,count FROM ipees ORDER BY count desc"):
            print(row["ip"], ";", row["count"])
    else:
        for row in cur.execute("SELECT ip,count FROM ipees ORDER BY count"):
            print(row["ip"], ";", row["count"])


###############################################################################
def print_total_sqlite(cur):

    for row in cur.execute("SELECT count(count) as total FROM ipees"):
        print("Anzahl:  ", row["total"])



###############################################################################
def print_ips():
    #IPs ausgeben:
    print("IPs; Anzahl")
    for mkeys in fdict:
        anzahl_ips = fdict[mkeys]
        str(anzahl_ips)
        print("%s; %d" % (mkeys,anzahl_ips))


###############################################################################
def print_dates():
    #nach Datum ausgeben
    #arrayDateLength = len(arrayDate)
    sorted_x = sorted(hashDate.items(), key=operator.itemgetter(1))
    tupleSize = len(sorted_x)

    print("\n by Date:")
    for x in range(tupleSize):
        #str(dkeys)
        myDate, myCount = sorted_x[x]
        print("%s: %s" % (myDate, myCount))
    #for x in arraydate:
    #    print(x)


###############################################################################
#def usage():
#    print("Usage: python3 failstat.py filename\n")
#    exit(1)


###############################################################################
def nofile(filename):
    print("No such File: " + filename +":\n")
    exit(1)

###############################################################################
###############################################################################
if __name__ == "__main__":
    main()
