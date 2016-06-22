#!/usr/bin/env python

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        (year, temperature) = (line[0:4],  line[8:])
        print "%s\t%s" % (year, temperature)

if __name__=='__main__':
    main()

