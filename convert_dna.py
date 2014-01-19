#!/usr/bin/python

import sys

MAPPING = {
    'A' : 2,
    'G' : 1,
    'C' : -1,
    'T' : -2
}

def convert(line):
    series = [0]
    for char in line:
        series.append(series[-1] + MAPPING[char])
    return series

if __name__ == "__main__":
    print convert(sys.stdin.readline())
