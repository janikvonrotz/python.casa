

import os

basepath = '/home/janikvonrotz/janikv.cloud/python.casa'

def walk(path):
    print("Ausgabe ", path, ":")
    for entry in os.listdir(path):
        fullpath = os.path.join(path, entry)
        if os.path.isdir(fullpath) and entry != ".git":
            print(entry)
            walk(fullpath)

walk(basepath)