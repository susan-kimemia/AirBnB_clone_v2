#!/usr/bin/python3
"""Distributes an archive to web servers using the function do_deploy"""
from fabric.api import *
from os.path import exists

env.hosts = ["100.25.17.77", "100.24.242.170"]
env.user = "ubuntu"
env.key_filename = '~/.ssh/0-RSA_key'


def do_deploy(archive_path):
    """Distributes an archive to web servers"""

    # Check if the archive file exists
    if not exists(archive_path):
        return False
    try:
        # Upload the archive to /tmp/ on the web server
        put(archive_path, "/tmp/")

        # Extract the archive to /data/web_static/releases/
        # <filename without extension>/
        archive_file = archive_path[9:]
        release_folder = "/data/web_static/releases/" + archive_file[:-4]
        run("sudo mkdir -p {}".format(release_folder))
        run("sudo tar -xzf /tmp/{} -C {}".format(archive_file, release_folder))

        # Delete the archive from the web server
        run("sudo rm /tmp/{}".format(archive_file))

        # Move the contents to the proper location
        run("sudo mv {}/web_static/* {}".format(
            release_folder, release_folder))

        # Remove the symbolic link /data/web_static/current
        run("sudo rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current
        run("sudo ln -s {} /data/web_static/current".format(release_folder))

        print("New version deployed!")
        return True
    except Exception as e:
        return False
