#!/usr/bin/env python3

import argparse
from QuitMerge import QuitMerge

if __name__ == "__main__":

    # command line parameters
    # This tool can be used for git-merge
    # git-merge:
    #   if using as git-merge, the parameters are:
    #   path old-file new-file
    #
    # local is the local branch to merge
    # remote is the remote branch to merge
    parser = argparse.ArgumentParser()
    parser.add_argument('base', nargs='?', type=str)
    parser.add_argument('local', nargs='?', type=str)
    parser.add_argument('remote', nargs='?', type=str)

    args = parser.parse_args()

    quitmerge = QuitMerge()
    if (args.base and args.local and args.remote):
        quitmerge.merge(args.base, args.local, args.remote)
    else:
        exit(1)
