#!/usr/bin/python3
# Fabric script (based on the file 2-do_deploy_web_static.py)
# that creates and distributes an archive to your web servers,
# using the function deploy

import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run
from fabric.api import local 

env.hosts = ["34.75.191.53", "3.94.192.73"]


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

def do_deploy(archive_path):
    """
    Distributes an archive to a web server.
    archive_path: The path of the archive to distribute
    """
    if os.path.isfile(archive_path) is False:
        return False

    file = archive_path.split("/")[-1]
    name_file = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name_file)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name_file)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/"
           .format(name_file, name_file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name_file)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name_file)).failed is True:
        return False
    return True

def deploy():
    """ Function that creates and distributes an archive to your web servers"""
    try:
        save_path = do_pack()
        deploy_res = do_deploy(save_path)
        return (deploy_res)
    except:
        return False
