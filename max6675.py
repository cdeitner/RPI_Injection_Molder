import RPi.GPIO as GPIO
import time

# Initialize the control pins
def init_max6675 (tc_pins, sck=37, miso=35):
  global SCK
  SCK = sck
  global MISO
  MISO = miso
  GPIO.setup(sck, GPIO.OUT, initial = GPIO.LOW)
  GPIO.setup(miso, GPIO.IN)
  for pin in tc_pins:
    GPIO.setup(pin, GPIO.OUT, initial = GPIO.HIGH)

def read_temp (tc):
  data = 0
  GPIO.output(tc, GPIO.LOW)
  time.sleep(0.00001) # is this needed? 100ns min in datasheet
  GPIO.output(SCK, GPIO.HIGH)
  GPIO.output(SCK, GPIO.LOW)
  
  for i in range(11, -1, -1):
    GPIO.output(SCK, GPIO.HIGH)
    data = data + (GPIO.input(MISO) * (2 ** i))
    GPIO.output(SCK, GPIO.LOW)
    
  GPIO.output(SCK, GPIO.HIGH)
  error = GPIO.input(MISO)
  GPIO.output(SCK, GPIO.LOW)

  for i in range(2):
      GPIO.output(SCK, GPIO.HIGH)
      time.sleep(0.00001) # is this needed? 100ns min in datasheet
      GPIO.output(SCK, GPIO.LOW)  
    
  GPIO.output(tc, GPIO.HIGH)
  
  temp = data * 0.25
  
  if error != 0:
      return -cs_no
  else:
      return temp
  
