#!/usr/bin/env python
"""
reloadall.py: transitively reload nested modules
"""
import types
from imp import reload

def status(module):
    print("reloading " + module.__name__)

def transitive_reload(module, visited):
    if not module in visited:           # Trap cycles and duplicates
        status(module)                  # Reload this module
        reload(module)                  # and visit children
        visited[module] = None          # Using a valueless dict like a set
        for attrobj in module.__dict__.values():      # for each attr
            if type(attrobj) == types.ModuleType:     # Recur if module
                transitive_reload(attrobj, visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

# a main for if ran instead of imported
if __name__ == '__main__':
    import reloadall26                  # Need to import self to test on self
    reload_all(reloadall26)             # Should reload this and types

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
