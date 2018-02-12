from microphone_recognition import *
from pyfirmata_trans import *

brightness = 0

while (1):
	txt = audioToText()
	brightness = control(txt, brightness)
	print 'Current Brightness: ', brightness