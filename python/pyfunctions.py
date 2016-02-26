#!/usr/bin/env python3.5


def okay(happy, year):
    import subprocess
    subprocess.run([happy, year])
    return
def dns(host):
    import subprocess
    subprocess.run(["host", host])
    return
