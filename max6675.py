import RPi.GPIO as GPIO
import time

# Initialize the control pins
def init_max6675 (sck=37, miso=35, tc_pins):
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(sck, GPIO.OUT, initial = GPIO.LOW)
  GPIO.setup(miso, GPIO.IN)
  for pin in tc_pins:
    GPIO.setup(pin, GPIO.OUT, initial = GPIO.HIGH)

def read_temp (tc):
  GPIO.output(tc, GPIO.LOW)
  time.sleep(0.00001) # is this needed?
  GPIO.output(sck, GPIO.HIGH)
  
  
