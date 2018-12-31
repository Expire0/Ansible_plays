#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Randomly create a password with openssl and add some salt

@author: Expire0(airtime166,Openkb)
"""

from subprocess import Popen,PIPE
import shlex, random


def Pass():
    bogus = ['a$%', 'b&*', 'cF%$', 'dG^D', 'eG^&^']
    cmd = "openssl  rand -base64 10"
    args = shlex.split(cmd)
    gen = Popen(args, stdout=PIPE)
    print( random.choice(bogus) + gen.communicate()[0].decode("UTF-8"))
    
if __name__ == "__main__":
    Pass()
