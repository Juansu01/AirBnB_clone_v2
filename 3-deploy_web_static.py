#!/usr/bin/python3
"""This module defines a function that compacts a directory """
from fabric.api import local
from datetime import datetime
from fabric.api import env, put, run
env.user = 'ubuntu'
env.hosts = ['35.185.54.141', '54.165.248.35']


def do_pack():
    """Pack directory """
    the_time_is_now = datetime.now()
    ye = the_time_is_now.year
    mo = the_time_is_now.month
    da = the_time_is_now.day
    ho = the_time_is_now.hour
    mi = the_time_is_now.minute
    se = the_time_is_now.second
    file_name = "{}_{}{}{}{}{}{}.tgz".format(
        "web_static", ye, mo, da, ho, mi, se)
    local("mkdir -p versions")
    local("tar -cavf versions/{} web_static".format(file_name))


def do_deploy(archive_path):
    """ This function deploys the archive made in do pack"""
    if not archive_path:
        return False
    name_of_file = archive_path[9:]
    print(name_of_file)
    put(archive_path, "/tmp/{}".format(name_of_file))
