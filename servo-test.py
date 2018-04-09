#!/usr/bin/python
import time
from Sunfounder_PWM_Servo_Driver import PWM

pwm = PWM(0x40, True)
pwm.setPWMFreq(60)


# Min found around 150
# Max found around 700
servoMin = 150
servoMax = 700



print "Hello, servo-world"

while (True):
  # Change speed of continuous servo on channel O
  pwm.setPWM(0, 0, servoMin)
  time.sleep(1)
  pwm.setPWM(0, 0, servoMax)
  time.sleep(1)
  print "Looping!"

