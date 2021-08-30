#!/usr/bin/python3
# Fabric script (based on the file 3-deploy_web_static.py)
# that deletes out-of-date archives, using the function do_clean

import os
from fabric.api import env
from fabric.api import lcd
from fabric.api import run


env.hosts = ["34.75.191.53", "3.94.192.73"]


def do_clean(number=0):
    """
    Delete out-of-date archives.
    number: The number of archives to keep.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))

    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [run("rm ./{}".format(a)) for a in archives]

    with lcd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
