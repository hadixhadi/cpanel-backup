#!/bin/bash
mysqlcheck --repair --all-databases
mysql -e "show databases" > /root/databases_list.txt
sed -i '1d' databases_list.txt
mkdir db_bc
cd db_bc
mkdir `date +"%y-%m-%d"`
cd `date +"%y-%m-%d"`
while read line;do
        if [[ $line != "information_schema" && $line != "performance_schema" ]]; then
                mysqldump $line > $line.sql
        fi
done </root/databases_list.txt 
