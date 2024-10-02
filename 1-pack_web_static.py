#!/usr/bin/python3
"""
Compressing the web_static folder into a .tgz archive using Fabric.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo.
    """

    if not os.path.exists("versions"):
        os.makedirs("versions")

    now = datetime.now()

    filename = (f"web_static_{now.year}{now.month:02}"
                f"{now.day:02}{now.hour:02}{now.minute:02}{now.second:02}.tgz"
                )

    archive_path = f"versions/{filename}"

    try:
        local(f'tar -cvzf {archive_path} web_static')
        print(f"Packing web_static to {archive_path}")
        return archive_path
    except Exception as e:
        print(f'Failed to create archive: {e}')
        return None
