#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the
# contents of the web_static folder of your AirBnB Clone rep
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Create a tar gzipped archive of the directory web_static.
    """
    file = 'versions/web_static_{}.tgz'\
           .format(datetime.now().strftime("%Y%m%d%H%M%S"))

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
