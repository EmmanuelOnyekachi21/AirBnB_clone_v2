#!/usr/bin/python3
"""
distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import env, put, run
import os

# Set the hosts for the fabric environment
env.hosts = ['35.168.3.245', '54.85.28.0']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
    script that distributes an archive to your web servers.
    """
    if not os.path.exists(archive_path):
        return False
    try:
        # Upload the archive to the /tmp/directory
        put(archive_path, '/tmp/')

        # Get the filename without the extension
        filename = archive_path.split('/')[-1]
        name = filename.split('.')[0]

        # Create the release directory
        run(f'mkdir -p /data/web_static/releases/{name}/')

        # Uncompress the archive to the release directory
        run(f'tar -xzf /tmp/{filename} -C'
            f'/data/web_static/releases/{name}/')
        # delete the archive from the web server
        run(f'rm /tmp/{filename}')

        # Move the files from the extracted folder to the release directory
        run(f"mv /data/web_static/releases/{name}/web_static/*"
            f" /data/web_static/releases/{name}/")

        # remove the now-empty web_static folder
        run(f'rm -rf /data/web_static/releases/{name}/web_static')

        # Delete the current symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link to the latest release
        run(f'ln -s /data/web_static/releases/{name}/'
            f'/data/web_static/current')

        return True
    except Exception as e:
        return False
