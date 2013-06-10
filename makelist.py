#!/usr/bin/env python

import sys, re
from itertools import tee, izip

def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

def is_flw(word):
    return len(word) == 4 and word.isalpha()

def addwords(words, f):
    for word, associations in pairwise(f.read().splitlines()):
        if is_flw(word):
            ass = [a.strip() for a in re.split(r'[\\|]', associations)]

            current_word = words.get(word, [])
            for v, w in pairwise(ass):
                if is_flw(v):
                    if not v in current_word:
                        current_word.append(v)
            words[word] = current_word


def generate(rsfile, srfile):
    words = {}
    addwords(words, rsfile)
    addwords(words, srfile)
    return words

if __name__=="__main__":
    if len(sys.argv) != 3:
        print "Usage: %s <rs_concise> <sr_concise>" % sys.argv[0]
        sys.exit(0)

    rsfilename, srfilename = sys.argv[1:]
    words = generate(open(rsfilename), open(srfilename))
    for word in sorted(words.keys()):
        if len(words[word]) > 0:
            print "%s: %s" % (word, ", ".join(sorted(words[word])))
    

