import sys
import os.path
import operator
import sqlite3
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="file to work with")
parser.add_argument("-d", "--descending", help="sort descending", action="store_true")
parser.add_argument("-c", "--csv", help="output csv", action="store_true")
args = parser.parse_args()

def main():
    """ Main program """
    #check arguments
    if args.file:
        print("file arg: " + args.file)
    if args.csv:
        print("-c csv argument active")
    if args.descending:
        print("-d descending argument active")




###############################################################################
if __name__ == "__main__":
    main()
