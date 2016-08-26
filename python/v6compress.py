#!/usr/bin/env python3

#compress v6 expanded addresses in bulk.  pulls from a local file and based on python3

import ipaddress
import sys


with open('mas2') as mas:
    v6 = mas.read().splitlines()
    for i in v6:
        hey = ipaddress.ip_address(i)
        print(hey.compressed)
