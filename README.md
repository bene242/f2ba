# f2ba
Tool for analyzing fail2ban logs

Goals: 
- become a better programmer
- a quick way to analyze fail2ban logs to identify hacking attemps. 
- block suspicous IPs via iptables (forever)

If someone wants to help. feel free to contact me: bene_k27 at yahoo.de

Files:

read_f2blog_write_mysql.py

reads the fail2ban logfile and writes all banned entries in a mysql database. Should run somewhere (e.g. on the server directy) where the fail2ban logfiles are accessible. 
