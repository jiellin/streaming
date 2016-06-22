#!/usr/bin/env python

import re
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        (year, temp, q) = (line[15:19], line[87:92], line[92:93])
        if(temp != "+9999" and re.match("[01459]", q)):
            print "%s\t%s" % (year, temp)


if __name__=='__main__':
    main()

