#!/usr/bin/env python

import os
import re
import urllib2

#base= "http://dl.film2movie.biz/serial/The%20Walking%20Dead/S01/"
get = raw_input("enter url: ")
response = urllib2.urlopen(get)
html = response.read()
mas = re.compile('<[a-z]\s\w{3,4}\=".*a\>')
check = mas.findall(html) 


for i in check:
    mov= i
    prep = re.compile('>[a-z]?[A-Z]?.*.mkv')
    prep1 = prep.findall(mov)
    for p in prep1:
        ok= p.replace('>','')
        print   get + ok
