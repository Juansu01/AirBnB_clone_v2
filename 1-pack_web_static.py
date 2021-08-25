#!/usr/bin/python3
"""This module defines a function that compacts a directory """
from fabric.api import local
from datetime import datetime


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
