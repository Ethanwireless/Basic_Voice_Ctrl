import pyfirmata
from os import system 

DELAY = 2 # A 2 seconds delay

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0, 
# On Windows: \\.\COM1, \\.\COM2
PORT = '/dev/tty.usbmodem1421' # hardcoded
print ('Opening Port')

# Creates a new board 
board = pyfirmata.Arduino(PORT)
print ('Board Connected')

pin = board.get_pin('d:11:p')

def lightOn():
	pin.write(1) # Set the LED pin to 1 (HIGH)
	return 1

def lightOff():
	pin.write(0) # Set the LED pin to 1 (HIGH)
	return 0

def lightMid():
	pin.write(0.5) # Set the LED pin to analog middle value
	return 0.5

def down(brightness):
	brightness -= 0.25
	if (brightness < 0):
		brightness = 0
	pin.write(brightness)
	return brightness

def up(brightness):
	brightness += 0.25
	if (brightness > 1):
		brightness = 1
	pin.write(brightness)
	return brightness

def control (txt, brightness):
	if (txt == 'turn on'):
		lightOn()
		brightness = 1
		system('say '+'Light is turned on')

	elif (txt == 'turn off'):
		lightOff()
		brightness = 0
		system('say '+'Light is turned off')

	elif (txt == 'middle'):
		lightMid()
		brightness = 0.5
		system('say '+'Light is turned half way')

	elif (txt == 'turn up'):
		brightness = up(brightness)
		system('say '+
			'Brightness is at {0} percent'.format(brightness*100))

	elif (txt == 'turn down'):
		brightness = down(brightness)
		system('say '+
			'Brightness is at {0} percent'.format(brightness*100))

	return brightness
