#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import re
from time import sleep
import socket
import string
import struct
import mysql.connector


debug = 1

def ip2int(theip):
    packetIP = socket.inet_aton(theip)
    return struct.unpack("!L", packetIP)[0]


def checkip(ip_int, date, mydbconn):
    mycursor = mydbconn.cursor(buffered = True)
    mycursor.execute("SELECT * FROM fail2ban where ip_int='" + str(ip_int) + "' and date = '" + date  + "'")
    #print("SELECT * FROM fail2ban where ip_int=" + str(ip_int) + " and date = " + date )
    myresult = mycursor.fetchone()
    #if debug==1:
    #    print(myresult)
    if myresult == None:
        return 0
    else:
        return 1

def add_entry(the_ip, the_ip_int, the_date, the_time, mydbconn):
    mycursor = mydbconn.cursor()
    sql = "insert into fail2ban (ip,ip_int,date, time) values (%s,%s,%s,%s)"
    val = (the_ip, the_ip_int, the_date,the_time)
    #sql_simple="insert into fail2ban (ip,ip_int,date, time) values ('"+the_ip+"','"+str(the_ip_int)+"','"+the_date+"','"+the_time+"')"
    #print("insert into fail2ban (ip,ip_int,date, time) values ('"+the_ip+"','"+str(the_ip_int)+"','"+the_date+"','"+the_time+"')")
    #if debug==1:
    #    print("SQL: "+sql+" Values: " +str(val[1]))
    mycursor.execute(sql, val)
    #mycursor.execute(sql_simple)
    mydbconn.commit()

def main():
    """ Main program """
    mydb = mysql.connector.connect(
        host="192.168.178.58",
        user="fail",
        password="2ban",
        database="fail2ban"
    )

    numfound = 0
    numnotfound = 0
    ipfound = []
    ipnotfound = []

    # Code goes over here.
    regex = re.compile("Ban")
    #fname = "/home/pi/fail2ban-jatos/fail2ban/fail2ban.log.1"
    #fname = "/home/pi/fail2ban.log.test"
    #fname = "/home/bene/github/f2ba/data/fail2ban.all.jatos"
    fname = "/home/bene/github/f2ba/data/fail2ban.test.jatos"
    with open(fname) as f:
        for line in f:
            line = line.rstrip()
            result = regex.search(line)
            if result:
                banline = line.split()
                time_long = banline[1].split(',')
                the_time = time_long[0]
                the_ip = banline[7]
                the_ip_int = ip2int(the_ip)
                the_date = banline[0]
                if debug==1:
                    print(the_date + " - " + the_time + " - " + the_ip + " - " + str(the_ip_int))

                if checkip(the_ip_int, the_date, mydb) == 1 :
                    if debug==1:
                        print("### FOUND! ###")
                        print (the_ip, the_date)
                    #print ip, date already in DB
                    # logfile : ip, date already in DB
                    numfound = numfound+1
                    ipfound.append(the_ip)
                else:
                    #logfile ip,date added
                    #insert into mysqldb
                    if add_entry(the_ip, the_ip_int, the_date, the_time, mydb) == 0:
                        if debug==1:
                            print("Something went wrong inserting")
                            return 1
                    else:
                        numnotfound = numnotfound+1
                        ipnotfound.append(the_ip)
                        if debug==1:
                            print("inserted")
                            print("** NOT FOUND! **")
                            print (the_ip, the_date)

    print("\ngefunden: "  + str(numfound) + "  nicht gefunden: " + str(numnotfound))
    if debug == 1:
        print("\nIPs gefunden: ")
        for x in ipfound:
            print(x)
        print("\nIPs NICHT gefunden: ")
        for y in ipnotfound:
            print(y)
    return 0

if __name__ == "__main__":
    main()
