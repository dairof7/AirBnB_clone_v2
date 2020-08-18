#!/usr/bin/python3
"""Distributes an archive to your web servers."""

from fabric.api import put, run, env
from os import path


env.hosts = ['35.227.29.60', '54.196.131.110']


def do_deploy(archive_path):

    _path = archive_path.split('/')
    path_with_ext = _path[1]
    path_no_ext = _path[1].split('.')[0]

    if not path.exists(archive_path):
        return False

    try:
        # upload file to /tmp/ on webservers
        put(archive_path, '/tmp')
        # create dir
        run("sudo mkdir -p /data/web_static/releases/" + path_no_ext + '/')
        # uncompress file in
        run("sudo tar -xzf /tmp/" + path_with_ext +
            ' -C /data/web_static/releases/'
            + path_no_ext + '/')
        # Delete the archive from the web server
        run("sudo rm /tmp/" + i + ".tgz")
    except Exception:
        return False

    return True
