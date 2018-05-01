#!/usr/bin/python
from pyo import *
from shoey import openMouthPercent

s = Server().boot()
s.start()
path = "./hedberg-peace.inp"
print "path: " + path
sf = SfPlayer(path, loop=False, mul=.4).out()
fol = Follower(sf, freq=30)

def snapshot():
    val = fol.get()
#    print "amplitude: %.2f" % (val)
    openMouthPercent(val)

pat = Pattern(snapshot, time=.01).play()

# Opens the server graphical interface.
# s.gui(locals())
