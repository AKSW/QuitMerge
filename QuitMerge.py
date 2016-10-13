#!/usr/bin/env python3

import sys

class QuitMerge:

    local = None
    remote = None
    merged = None
    base = None

    def __init__ (self):
        True

    def merge (self, base, local, remote):

        print(base)
        print(local)
        print(remote)

        print ("base")
        with open(base) as fileBase:
            for line in fileBase:
                print(line)

        print ("local")
        with open(local) as fileBase:
            for line in fileBase:
                print(line)

        print ("remote")
        with open(remote) as fileBase:
            for line in fileBase:
                print(line)

        fileBase = open(base, 'r')
        fileLocal = open(local, 'r')
        fileRemote = open(remote, 'r')

        # use list() instead of readlines() resp. I use set() in this case
        # https://stupidpythonideas.blogspot.de/2013/06/readlines-considered-silly.html

        addA = set(fileLocal) - set(fileBase)
        addB = set(fileRemote) - set(fileBase)
        intersect = set(fileLocal).intersection(set(fileRemote))
        fileBase.close()
        fileLocal.close()
        fileRemote.close()

        merged = sorted(intersect.union(addA).union(addB))
        # remote blank lines
        merged = list(filter(lambda line: line.strip(), merged))

        print ("merged")
        for line in merged:
            print(line)

        with open(local, 'w') as fileMerged:
            fileMerged.writelines(merged)

        # merge result has to be written to *local*

        return
