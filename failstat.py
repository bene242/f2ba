#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os.path
import operator
import sqlite3



fname =""
fdict = {"0.0.0.0": 0}
hashDate = {"2020-00-00": 0}
#arrayDate[0] = "2020-00-00"


###############################################################################
###############################################################################
def main():
    """ Main program """
    global fname, fdict, hashDate
    #check if only 1 Argument
    if (len(sys.argv) != 2):
        usage()
    fname = sys.argv[1]
    if (os.path.isfile(fname) != True):
        nofile(fname)


    fobj = open(fname)
    for line in fobj:
        fdate, fip = (line.split( ))
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
    fobj.close()

    ### save in sqlite3
    save_in_sqlite()
#    print_ips()


###############################################################################
def save_in_sqlite():
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

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

    for row in cur.execute("SELECT ip,count FROM ipees ORDER BY count"):
        print(row["ip"], " - ", row["count"])

    cur.close()
    conn.close()


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
def usage():
    print("Usage: python3 failstat.py filename\n")
    exit(1)


###############################################################################
def nofile(filename):
    print("No such File: " + filename +":\n")
    exit(1)

###############################################################################
###############################################################################
if __name__ == "__main__":
    main()
