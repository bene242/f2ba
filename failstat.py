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


    print_ips()

def save_in_sqlite():
    conn = sqlite3.connect('fail2ban.sqlite')
    for mkeys in fdict:
        anzahl_ips = fdict[mkeys]
        conn.execute('insert into ips (ip,anzahl) values ("192.000.000.255",3)')
    conn.commit()

    conn.close()

def print_ips():
    #IPs ausgeben:
    for mkeys in fdict:
        anzahl_ips = fdict[mkeys]
        str(anzahl_ips)
        #if anzahl_ips != 1 and anzahl_ips != 2:
        if anzahl_ips not in [1,2,3]:
            print("%s: %d" % (mkeys,anzahl_ips))
        #print(fdict[mkeys])

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


def usage():
    print("Usage: python3 filename\n")
    exit(1)

def nofile(filename):
    print("No such File: " + filename +":\n")
    exit(1)

if __name__ == "__main__":
    main()
