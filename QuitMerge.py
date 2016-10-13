#!/usr/bin/env python3

class QuitMerge:

    def __init__ (self):
        True

    def merge (self, base, local, remote):
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
        # remove blank lines
        merged = list(filter(lambda line: line.strip(), merged))

        # merge result has to be written to *local*
        with open(local, 'w') as fileMerged:
            fileMerged.writelines(merged)

        return
