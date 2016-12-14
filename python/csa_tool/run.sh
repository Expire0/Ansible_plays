#!/usr/bin/bash

mas=0
run='/usr/bin/date'

rm -rf check
echo /var/log/mas.5858585.log
echo masekela
while [ $mas -lt 10 ] ; do
       $run >> check  
       sleep 5
done