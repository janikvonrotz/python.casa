#!/usr/bin/env python3
import getpass
from datetime import datetime
from pathlib import Path

user = getpass.getuser()
now = datetime.now()
home = Path.home()
testfile = home.joinpath('testpython-test-file.tmp')

with open(testfile, 'wt') as f:
    f.write(user + '\n')
    f.write(str(now) + '\n')
