#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
regex = re.compile("Ban")
with open("../data/fail2ban.all.jatos") as f:
    for line in f:
        line = line.rstrip()
        result = regex.search(line)
        if result:
            arrg = line.split()
            print(arrg[0]+" "+arrg[7])
            exit(0)
