#!/usr/bin/env python
import sys

def main():
    for line in sys.stdin:
        print "%s\t%s" % (line.strip(), "")


if __name__=='__main__':
    main()

