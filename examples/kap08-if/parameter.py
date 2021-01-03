#!/usr/bin/env python3
import platform, sys
from glob import glob
iswin = platform.system() == 'Windows'
if len(sys.argv)<=1:
    print('Es wurden keine Parameter übergeben.')
else:
    for para in sys.argv[1:]:
        if iswin and ('?' in para or '*' in para):
            print('Parameter: ', glob(para))
        else:
            print('Parameter:', para)
