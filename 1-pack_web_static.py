#!/usr/bin/python3
"""  Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ Function that generates a .tgz archive """
    date = datetime.now().strftime('%Y%m%d%H%M%S')

    try:
        local('mkdir -p versions')
        local('tar -cvzf versions/web_static_{}.tgz web_static'.format(date))
        return 'versions/{}.tgz'.format(date)
    except:
        return None
