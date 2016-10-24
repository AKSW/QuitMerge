from abc import ABCMeta
from QuitMerger import QuitMerger

class ThreewayMerge(metaclass=ABCMeta):

    def __init__ (self):
        True

    def merge (self, base, local, remote):
        # use list() instead of readlines() resp. I use set() in this case
        # https://stupidpythonideas.blogspot.de/2013/06/readlines-considered-silly.html
        fileBase = open(base, 'r')
        fileLocal = open(local, 'r')
        addA = set(fileLocal) - set(fileBase)
        fileBase.close()
        fileLocal.close()

        fileBase = open(base, 'r')
        fileRemote = open(remote, 'r')
        addB = set(fileRemote) - set(fileBase)
        fileBase.close()
        fileRemote.close()

        fileLocal = open(local, 'r')
        fileRemote = open(remote, 'r')
        intersect = set(fileLocal).intersection(set(fileRemote))
        fileLocal.close()
        fileRemote.close()

        merged = sorted(intersect.union(addA).union(addB))
        # remove blank lines
        merged = list(filter(lambda line: line.strip(), merged))

        # merge result has to be written to *local*
        with open(local, 'w') as fileMerged:
            fileMerged.writelines(merged)

        return

ThreewayMerge.register(QuitMerger)
