from abc import ABCMeta
from QuitMerger import QuitMerger

class ThreewayMerge(metaclass=ABCMeta):

    def __init__ (self):
        True

    def merge (self, base, local, remote):
        # use list() instead of readlines() resp. I use set() in this case
        # https://stupidpythonideas.blogspot.de/2013/06/readlines-considered-silly.html
        with open(base, 'r') as fileBase:
            with open(local, 'r') as fileLocal:
                addA = set(fileLocal) - set(fileBase)

        with open(base, 'r') as fileBase:
            with open(remote, 'r') as fileRemote:
                addB = set(fileRemote) - set(fileBase)

        with open(local, 'r') as fileLocal:
            with open(remote, 'r') as fileRemote:
                intersect = set(fileLocal).intersection(set(fileRemote))

        merged = sorted(intersect.union(addA).union(addB))
        # remove blank lines
        merged = list(filter(lambda line: line.strip(), merged))

        # merge result has to be written to *local*
        with open(local, 'w') as fileMerged:
            fileMerged.writelines(merged)

        return

ThreewayMerge.register(QuitMerger)
