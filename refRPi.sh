#!/bin/bash
# Simple script for aggregate all "ban" IPs (on monitor-RPi)
# for statistics to a new file "fail2ban.all.ban.2"
# ----------------------------------------------------------------------

rm /home/pi/fail2ban-RPi/*

for ffile in /home/pi/f2bl/*
do
	cp $ffile /home/pi/fail2ban-RPi/
done

for ffile in /home/pi/fail2ban-RPi/*
do
	printf $ffile
	if [[ $ffile =~ "."gz$ ]];
	then
		gunzip $ffile
		printf "  -> unzipping... "
	fi
	printf "\n"
done

cat /home/pi/fail2ban-RPi/fail2ban.log \
	/home/pi/fail2ban-RPi/fail2ban.log.1 \
	/home/pi/fail2ban-RPi/fail2ban.log.2 \
	/home/pi/fail2ban-RPi/fail2ban.log.3 \
	/home/pi/fail2ban-RPi/fail2ban.log.4 \
	> /home/pi/fail2ban-RPi/fail2ban.all

grep Ban /home/pi/fail2ban-RPi/fail2ban.all > /home/pi/fail2ban-RPi/fail2ban.all.ban
#now we have
# 2020-03-01 00:13:53,293 fail2ban.actions        [593]: NOTICE  [sshd] Ban 112.220.238.3

cut -d ' ' -f 1,16 /home/pi/fail2ban-RPi/fail2ban.all.ban > /home/pi/fail2ban-RPi/fail2ban.all.ban.2
# now we have:
# 2020-02-08 182.139.134.107
