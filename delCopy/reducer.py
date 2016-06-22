#!/usr/bin/env python

import sys

def main():
    lastword = ""
    for line in sys.stdin:
        key, v= line.strip().split("\t")
        if lastword and lastword != key:
            print "%s\t%s" % (lastword, "")
        else:
            lastword=key

    if lastword:
        print "%s\t%s" % (lastword, "")


if __name__=="__main__":
    main()