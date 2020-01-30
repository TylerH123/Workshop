#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/test/")
sys.path.insert(0,"/var/www/test/test/")

import logging
logging.basicConfig(stream=sys.stderr)

from test import app as application