# f2ba
Tool for analyzing fail2ban logs

Goals:
- a quick way to analyze fail2ban logs to identify hacking attemps.
- block suspicous IPs via iptables (forever, like "iptables -A INPUT -s 123.123.0.0/16 -j DROP")


## Files:

###### read_f2blog_write_mysql.py

reads the fail2ban logfile and writes all banned entries in a mysql database. Should run somewhere (e.g. on the server directy) where the fail2ban logfiles are accessible.


###### failstat.py filename

reads the fail2ban logfile and write the output so stdout. Can also export in cvs formatting.
