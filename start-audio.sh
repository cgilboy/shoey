#!/bin/bash
export PATH=/home/pi/local/bin:${PATH}
export LD_LIBRARY_PATH=/home/pi/local/lib
jackd -m -p 32 -d dummy &
sleep 1
alsa_out -q1 2>&1 > /dev/null &
sleep 1
