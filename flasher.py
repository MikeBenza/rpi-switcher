import switcher

import RPi.GPIO as GPIO
import sys
import time

def main(pin, interval):
  print "Setting pin %d high" % pin
  switcher.setup()
  print "Ctrl+C to quit"

  value = False
  while (True):
    time.sleep(interval)
    switcher.set(pin, value)
    value = not value

if __name__ == "__main__":
  if len(sys.argv) == 3:
    pin = int(sys.argv[1])
    interval = float(sys.argv[2])
  else:
    print "Usage: %s PIN_NUMBER INTERVAL" % sys.argv[0]
    sys.exit(1)

  try:
    main(pin, interval)
  finally:
    GPIO.cleanup()