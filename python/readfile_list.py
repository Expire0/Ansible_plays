#!/usr/bin/env python2

import os

data = [line.strip() for line in open("/home/dhcp_primary", 'r')]
data1 = [line.strip() for line in open("/home/dhcp_secondary", 'r')]


def secondary():
    for  (name, grade) in zip(data1, data):
        print("./nrcmd -C " + name +  " ldap " + grade + " set  ")
        print("./nrcmd -C " + name +  " ldap " + grade + " set ")

def primary():
    for  (name, grade) in zip(data1, data):
        print("./nrcmd -C " + grade +  " ldap " + name + " set  ")
        print("./nrcmd -C " + grade +  " ldap " + name + " set  ")

primary()
