#!/usr/bin/python

# ========================================================
# VFD Modular Clock - Raspberry PI Edition
# 
# (C) 2013 Akafugu Corporation
# (C) 2013 William B Phelps - wm@usa.net
#
#
# This program is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# 
# fourletterword.py

import RPi.GPIO as GPIO
import sched, signal, time, sys
import random
from datetime import datetime
from vfdspi import *

def handleSigTERM(signum, frame):
	clear() # clear
	exit(0)

def handleCtrlC(signum, frame):
	clear() # clear
	exit(0)

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

    setBrt(10) # max brightness
    setDots(0)
    clear()
    setScroll(1)

    signal.signal(signal.SIGTERM, handleSigTERM)
    signal.signal(signal.SIGINT, handleCtrlC)

    words = readwords(open(sys.argv[1]))
    word = random.choice(words.keys())
    while True:
        scroll(0, word, 0, 0.15)
        word = random.choice(words[word])
        time.sleep(0.5)

