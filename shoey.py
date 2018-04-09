#!/usr/bin/python
import time
from Sunfounder_PWM_Servo_Driver import PWM

pwm = PWM(0x40)
pwm.setPWMFreq(60)

# Min found around 150
# Max found around 700
servoMin = 150
servoMax = 700
servoMid = servoMin + (servoMax - servoMin) / 2

debug = True

mouthChannel = 0
headChannel = 4

def log(string):
  if debug:
    print string
  return

def setServoValue(channel, value):
  pwm.setPWM(channel, 0, value)
  log("Setting channel " + str(channel) + " to " + str(value))
  return
  
def setMouthOpen(o = True):
  if o:
    log("Opening mouth")
    openValue = servoMin + 120
    setServoValue(mouthChannel, openValue)
  else:
    log("Closing mouth")
    closedValue = servoMin
    setServoValue(mouthChannel, closedValue)
  return


W_LEFT = 0
W_CENTER = 1
W_RIGHT = 2
def wiggleInDirection(direction = W_CENTER):
  log("Wiggling " + str(direction))
  if direction == W_LEFT:
    setServoValue(headChannel, servoMid - 70)
  elif direction == W_CENTER:
    setServoValue(headChannel, servoMid)
  elif direction == W_RIGHT:
    setServoValue(headChannel, servoMid + 70)
  return

def laugh(count = 3):
  for x in range(0, count):
    setMouthOpen(True)
    time.sleep(0.25)
    setMouthOpen(False)
    time.sleep(0.25)

  wiggleInDirection(W_LEFT)
  time.sleep(0.15)
  wiggleInDirection(W_RIGHT)
  time.sleep(0.15)
  wiggleInDirection(W_LEFT)
  time.sleep(0.15)
  wiggleInDirection(W_CENTER)
  return

print "For shoeth!"

wiggleInDirection(W_CENTER)

while (True):
  laugh()
  time.sleep(3)
  print "Looping!"

