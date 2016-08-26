#!/usr/bin/env python3

#compress v6 expanded addresses in bulk.  pulls from a local file and based on python3

import ipaddress
import sys


with open('<file>') as mas:
    v6 = mas.read().splitlines()  #remove newline \n 
    for i in v6:
        hey = ipaddress.ip_address(i)
        print(hey.compressed)


####cleaner way to do it with user defining the file 

#!/usr/bin/env python3

#compress v6 expanded addresses in bulk.  pulls from a local file and based on python3

import ipaddress
import sys
menu= input("Enter 1 for v6 compression:  ")
menu1 = int(menu)

if menu1 == 1:
    getme = input("filename: ")

    def v6compress(m):
        i=m
        with open(i) as mas:
            v6 = mas.read().splitlines()
            for i in v6:
                hey = ipaddress.ip_address(i)
                print(hey.compressed)

    v6compress(getme)

else:
    print ("nothing to do")
