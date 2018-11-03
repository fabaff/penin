"""Helpers for PenIn."""
import os

from cement.utils import fs
from tinydb import TinyDB


def extend_tinydb(app):
    """Add support for TinyDB."""
    app.log.info('Extending PenIn with TinyDB')
    db_file = app.config.get('penin', 'db_file')

    # Ensure that we expand the full path
    db_file = fs.abspath(db_file)
    app.log.info('TinyDB database file is: {}'.format(db_file))

    # Ensure our parent directory exists
    db_dir = os.path.dirname(db_file)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    app.extend('db', TinyDB(db_file))
