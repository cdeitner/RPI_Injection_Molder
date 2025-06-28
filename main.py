import max6675
import RPi.GPIO as GPIO
import time

# Use board pin numbering
GPIO.setmode(GPIO.BOARD)

# List of CS Pins for TCs
tcpins = [7]

# SCK Pin (default 37), MISO Pin (default 35)
max6675.init_max6675(tcpins)

while(1):  
  temp = max6675.read_temp(7)
  print(temp)
  time.sleep(1)
  



