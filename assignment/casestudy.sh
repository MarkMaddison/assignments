#!/bin/bash
user=$(whoami)
sudo echo "welcome $user"
time_today=$(date)
echo  $user $time_today >> AccessLog.txt
FILE=/usr/bin/python3
if test -f "$FILE"; then
    echo "$FILE exists."
else
    sudo yum install python3 -y
fi
sudo wget https://raw.githubusercontent.com/MarkMaddison/assignments/master/assignment/phonebook.py
