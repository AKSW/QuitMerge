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

        with open(base) as fO:
            for line in fO:
                print(line)

        print ("diff O:A")
        fO = open(base, 'r')
        fA = open(local, 'r')
        delta = self.delta(fO, fA)
        fO.close()
        fA.close()

        print ("set")
        print ("add")
        for line in delta["add"]:
            print(line)
        print ("delete")
        for line in delta["delete"]:
            print(line)


        print ("diff O:B")

        fO = open(base, 'r')
        fB = open(remote, 'r')
        delta = self.delta(fO, fB)
        fO.close()
        fB.close()

        print ("set")
        print ("add")
        for line in delta["add"]:
            print(line)
        print ("delete")
        for line in delta["delete"]:
            print(line)

        # merge result has to be written to *local*

        return

    def delta(self, local, remote):
        # use list() instead of readlines()
        # https://stupidpythonideas.blogspot.de/2013/06/readlines-considered-silly.html
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
