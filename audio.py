#!/usr/bin/python
from pyo import *
from shoey import openMouthPercent
from math import log10

s = Server(buffersize=2048).boot()
s.start()
path = "./hedberg-peace.inp"
print "path: " + path
sf = SfPlayer(path, loop=False, mul=.4).out()
#d = SDelay(sf, delay=0.1).out()
fol = Follower(sf, freq=30)

# smaller minDB -> lower overall values. not quite logical, probably indicates bug
minDB = 30

def dec2dbScale(dec):
    return max(0, (minDB + 10*log10(dec)) / minDB)

def snapshot():
    val = dec2dbScale(fol.get())
    print "amplitude: %.2f" % (val)
    openMouthPercent(val * 1.25)

pat = Pattern(snapshot, time=.1).play()

# Opens the server graphical interface.
# s.gui(locals())
