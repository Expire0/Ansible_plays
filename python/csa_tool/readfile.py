# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 03:52:35 2016

@author: mas
"""

file = open('check')

content= file.read()
if "Nov" in content:
    print(content)
else:
    print("not found")

file.close()