class QuitMerger:
    def merge (self, base, local, remote):
        '''
        base is the file in the merge base
        local is the file in the local branch into which the remote branch is merged
        remote is the file in the remote branch, which is merged into local

        the result of the merge has to be written to local
        '''
        return NotImplemented
