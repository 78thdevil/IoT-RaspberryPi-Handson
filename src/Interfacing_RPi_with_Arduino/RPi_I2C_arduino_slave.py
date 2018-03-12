#Raspberry pi    GND    ----------   GND     Arduino
#                3.3v   ----------   5v
#                SCL    ----------   A5
#                SDA    ----------   A4 
#
#
# http://blog.oscarliang.net/raspberry-pi-arduino-connected-i2c/
#

import smbus
import time

bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
	bus.write_byte(address, value)
	#bus.write_byte_data(address, 0, value)
	return -1

def readNumber():	
	number = bus.read_byte(address)
	#number = bus.read_byte_data(address, 1)
	return number

while True:
	var = int(input('\nEnter any value between 1-255: ')) #Enter 1 to see the LED on the Arduino Uno board Turn ON and OFF
	if not var:
		continue

	writeNumber(var)
	print ("RPi: Hi Arduino, I sent you ", var)
	# sleep one second
	time.sleep(1)

	number = readNumber()
	print ("Arduino: Hey RPi, I received a digit ", number)
