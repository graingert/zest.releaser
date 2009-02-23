"""Do the checks and tasks that have to happen before doing a release.
"""
import logging
import sys
import webbrowser
import tempfile
from commands import getoutput
import os

import utils

logger = logging.getLogger('longtest')


def show_longdesc():
    filename1 = tempfile.mktemp()
    filename2 = tempfile.mktemp()
    filename2 = filename2 + '.html'
    error = os.system('%s setup.py --long-description > %s' % (
            sys.executable, filename1))
    if error:
        logging.error('Error generating long description.')
        sys.exit()
    error = os.system('rst2html.py %s > %s' % (filename1, filename2))
    if error:
        # On Linux it needs to be 'rst2html', without the '.py'
        error = os.system('rst2html %s > %s' % (filename1, filename2))
    if error:
        logging.error('Error generating html. Please install docutils.')
        sys.exit()
    webbrowser.open(filename2)


def main():
    logging.basicConfig(level=utils.loglevel(),
                        format="%(levelname)s: %(message)s")
    show_longdesc()
