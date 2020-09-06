#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import re
from time import sleep


def main():
    """ Main program """
    # Code goes over here.
    regex = re.compile("Ban")

    fname = "fail2ban.log.test"
    with open(fname) as f:
        for line in f:
            line = line.rstrip()
            result = regex.search(line)
            if result:
                banline = line.split()
                time_long = banline[1].split(',')
                time_short = time_long[0]
                print(banline[0] + " - " + time_short + " - " + banline[7])
    return 0

if __name__ == "__main__":
    main()
