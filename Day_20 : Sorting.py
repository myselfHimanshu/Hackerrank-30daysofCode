#!/bin/python

import sys

def swap(a):
    numberOfSwaps = 0

    for i in range(n):
        for j in range(n-1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1]= a[j+1], a[j]
                numberOfSwaps+=1

        if numberOfSwaps == 0:
            break

    return a[0],a[-1],numberOfSwaps




n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
fe, le, ns = swap(a)

print 'Array is sorted in %d swaps.'%ns
print 'First Element: %d'%fe
print 'Last Element: %d'%le
