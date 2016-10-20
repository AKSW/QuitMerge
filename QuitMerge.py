from importlib import import_module

class QuitMerge:

    def __init__ (self):
        True

    def merge (self, base, local, remote, strategy="treeway"):
        module = strategy.title() + "Merge"
        merge = getattr(import_module(module), module)

        merger = merge()
        return merger.merge(base, local, remote)
