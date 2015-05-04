import RPi.GPIO as GPIO
import sys
import time

# GPIO channels corresponding to relays 0-7
GPIO_CHANNELS = [2, 3, 4, 17, 27, 22, 10, 9]

def toggle_one(relay, value):
  for (relay_id, channel) in enumerate(GPIO_CHANNELS):
    this_value = not ( False if relay < 0 else relay == relay_id and value)
    print "Setting relay %d (GPIO %d) to %s" % (relay_id, channel, this_value)
    GPIO.output(channel, this_value)

def set(relay_id, value):
    # False = on, True = off
    this_value = not value
    print "Setting relay %d (GPIO %d) to %s" % (relay_id, GPIO_CHANNELS[relay_id], this_value)
    GPIO.output(GPIO_CHANNELS[relay_id], this_value)

def setup():
  GPIO.setmode(GPIO.BCM)
  for xpin in GPIO_CHANNELS:
    GPIO.setup(xpin, GPIO.OUT)
