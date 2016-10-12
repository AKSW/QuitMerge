#!/usr/bin/env python3

import difflib
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

        addA = list(set(fileLocal) - set(fileBase))
        addB = list(set(fileRemote) - set(fileBase))
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

    def delta(self, local, remote):
        lineDelta = difflib.ndiff(sorted(list(local)), sorted(list(remote)))
        print(lineDelta)

        addSet = []
        deleteSet = []

        for line in lineDelta:
            if line.startswith('+ '):
                addSet.append(line[2:])
            if line.startswith('- '):
                deleteSet.append(line[2:])

        return {"add": addSet, "delete": deleteSet}
