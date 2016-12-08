#!/usr/bin/env python3.5


def okay(happy, year):
    import subprocess
    subprocess.run([happy, year])
    return
def dns(host):
    import subprocess
    subprocess.run(["host", host])
    return

def dipps(user, pass1):
    import subprocess
    import netaddr
    import os
#tool requires netaddr module

    scope = raw_input("which scope do you want to expand?  " )
    pg = raw_input("which primary dhcp:  ")
    pgs = pg.replace("pdhcp", "sdhcp")
    force = netaddr.IPNetwork(scope)
    all= list(force)
    for ccm in all:
        ccm = str(ccm)
        output= "nrcmd -C " + pg + " -N " + user + " -P " + pass1 +" lease " + ccm + " force-available "
        print  output
    return
def dippss():
    import subprocess

    for ccm in all:
             ccms = str(ccm)
             output= "nrcmd -C " + pg + " -N " + CNRUS + " -P " + CNRPA +" lease " + ccms + " force-available "

             print "nrcmd -C " + pgs + " lease " + ccms + " force-available "
             subprocess.call(output, shell=True)
