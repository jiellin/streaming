#!/usr/bin/env python

import sys

def main():
    (last_key, max_val) = (None, -sys.maxint)
    for line in sys.stdin:
        key, val = line.strip().split("\t")
        if key == last_key:
            max_val = max(max_val, int(val))
        else:
            if last_key:
                print "%s\t%s" % (last_key, max_val)
            (last_key, max_val) = (key, int(val))

    if last_key:
        print "%s\t%s" % (last_key, max_val)

if __name__=="__main__":
    main()