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
        # use list() instead of readlines()
        # https://stupidpythonideas.blogspot.de/2013/06/readlines-considered-silly.html
        OA = difflib.ndiff(sorted(list(fO)), sorted(list(fA)))
        print(OA)
        sys.stdout.writelines(OA)
        for line in OA:
            print(line)
        fO.close()
        fA.close()

        print ("diff O:B")

        fO = open(base, 'r')
        fB = open(remote, 'r')
        OB = difflib.ndiff(sorted(list(fO)), sorted(list(fB)))
        print(OB)
        sys.stdout.writelines(OB)
        for line in OB:
            print(line)
        fO.close()
        fB.close()

        # merge result has to be written to *local*

        return
