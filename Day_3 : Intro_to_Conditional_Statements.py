#!/bin/python

import sys


N = int(raw_input().strip())
if N%2!=0:
    print "Weird"
else:
    if N in range(2,6) or N>20:
        print "Not Weird"
    else:
        print "Weird"
