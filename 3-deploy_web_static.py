#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers, using the
function deploy """

from fabric.api import env, put, run, local
from datetime import datetime
import os.path


env.hosts = ['34.73.202.194', '54.82.109.39']


def do_pack():
    """ Function that generates a .tgz archive """
    date = datetime.now().strftime('%Y%m%d%H%M%S')

    try:
        local('mkdir -p versions')
        local('tar -cvzf versions/web_static_{}.tgz web_static'.format(date))
        return 'versions/web_static_{}.tgz'.format(date)
    except:
        return None


def do_deploy(archive_path):
    """ Function that distributes an archive to your web servers """
    if os.path.isfile(archive_path) is False:
        return(False)
    try:
        put(archive_path, '/tmp/')
        archive_name = archive_path.split('/')[-1]
        archive_name2 = archive_name.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}'.format(archive_name2))
        run('tar zxf /tmp/{} -C /data/web_static/releases/{}'.format(
            archive_name, archive_name2))
        run('rm /tmp/{}'.format(archive_name))
        run(
            'mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/'.format(
                archive_name2, archive_name2))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            archive_name2))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'.
            format(archive_name2))
        return True
    except:
        return False


def deploy():
    """ Function deploy  """
    try:
        return_path = do_pack()
        result = do_deploy(return_path)
        return result
    except:
        return False
