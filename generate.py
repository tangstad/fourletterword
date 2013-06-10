#!/usr/bin/env python

import sys, time, random

def readwords(f):
    words = {}
    lines = f.read().splitlines()
    for line in lines:
        word, l = line.split(": ")
        words[word] = l.split(", ")
    return words

if __name__=="__main__":
    if len(sys.argv) != 2:
        print "Usage: %s <wordfile>" % sys.argv[0]
        exit(0)

    words = readwords(open(sys.argv[1]))
    word = random.choice(words.keys())
    while True:
        print word
        word = random.choice(words[word])
        time.sleep(0.5)


