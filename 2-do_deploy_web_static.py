#!/usr/bin/python3
# Distributes an archive to your web servers


from datetime import datetime
from fabric.api import env, local, put, run
from os import path


env.hosts = ['34.228.37.117', '54.234.227.98']
env.user = 'ubuntu'


def do_pack():
    """
    folder to .tgz
    """
    mydate = datetime.now()
    myfile = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
        mydate.year,
        mydate.month,
        mydate.day,
        mydate.hour,
        mydate.minute,
        mydate.second
    )
    local('mkdir -p versions')
    answer = local('tar -cvzf ' + myfile + ' web_static')
    if answer.succeeded:
        return myfile
    return None


def do_deploy(archive_path):
    """Deploy archive to web servers"""
    if not path.exists(archive_path) and not path.isfile(archive_path):
        return False

    myspath = archive_path.split('/')[1].split(".")
    i = myspath[0]

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp')

        # create dir
        run("sudo mkdir -p /data/web_static/releases/" + i + "/")

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename
        # without extension> on the web server
        run("sudo tar -xzf /tmp/" + i + ".tgz" +
            " -C /data/web_static/releases/" + i + "/")

        # Delete the archive from the web server
        run("sudo rm /tmp/" + i + ".tgz")

        run("sudo mv /data/web_static/releases/" + i +
            "/web_static/* /data/web_static/releases/" + i + "/")

        # Delete the symbolic link
        run("sudo rm -rf /data/web_static/releases/" + i + "/web_static")
        run("sudo rm -rf /data/web_static/current")

        # Create a new the symbolic link
        run("sudo ln -s /data/web_static/releases/" + i +
            "/ /data/web_static/current")
    except Exception:
        return False

    return True
