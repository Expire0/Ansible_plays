#!/usr/bin/env python3.5

iurl = input("which domain?")

print ("testing modules")

from  pyfunctions import okay
from pyfunctions import dns
#okay("ps", "-ia")


dns(iurl)
