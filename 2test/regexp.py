#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
regex = re.compile("Ban")
with open("../data/fail2ban.all.jatos") as f:
    for line in f:
        result = regex.search(line)
        if result:
            print(line)
