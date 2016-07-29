#!/bin/python

import sys


n = int(raw_input().strip())
b = bin(n)[2:]
count = 0
while int(b)!=0:
    z = int(str(b)[1:]+'0',2)

    b = int(b,2)
    #print b,z
    b = (bin(b & z))[2:]
    #print b
    count+=1

print count
