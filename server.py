#!/usr/bin/env python
import os
import time
import RPi.GPIO as GPIO
import time

#naik = 6
#channel2 = 13
#turun = 19
#channel4 = 26

from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
	return 'Welcome to smartmeeting room'

@app.route('/on')
def turnon():

	#turn on TV and change input source and then turn on SOUNDBAR
	os.system('irsend SEND_ONCE PROJECTOR KEY_POWER')
	time.sleep(3)
	os.system('irsend SEND_ONCE PROJECTOR KEY_POWER')
	time.sleep(2)
	os.system('irsend SEND_ONCE TV KEY_POWER')
	time.sleep(2)

	
	turun = 19
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(turun, GPIO.OUT)
	
	#down
	def motor_on(pin):
	    GPIO.output(pin, GPIO.HIGH)  # Turn motor on
	
	def motor_off(pin):
	    GPIO.output(pin, GPIO.LOW)  # Turn motor off
	
	if __name__ == '__main__':
	    try:
	        motor_on(turun)
	        time.sleep(1)
	        motor_off(turun)
	        time.sleep(1)
	        motor_on(turun)
	        time.sleep(1)
	        motor_off(turun)
	        time.sleep(1)
	        GPIO.cleanup()
	    except KeyboardInterrupt:
	        GPIO.cleanup()
		
	return 'Turn On Success!'

@app.route('/off')
def turnoff():

	#turn off TV and change input source and then turn on SOUNDBAR
	os.system('irsend SEND_ONCE PROJECTOR KEY_POWER')
	time.sleep(3)
	os.system('irsend SEND_ONCE PROJECTOR KEY_POWER')
	time.sleep(2)
	os.system('irsend SEND_ONCE TV KEY_POWER')
	time.sleep(2)

	
	naik = 6
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(naik, GPIO.OUT)
	
	#up
	def motor_on(pin):
	    GPIO.output(pin, GPIO.HIGH)  # Turn motor on
	
	def motor_off(pin):
	    GPIO.output(pin, GPIO.LOW)  # Turn motor off
	
	if __name__ == '__main__':
	    try:
	        motor_on(naik)
	        time.sleep(1)
	        motor_off(naik)
	        time.sleep(1)
	        motor_on(naik)
	        time.sleep(1)
	        motor_off(naik)
	        time.sleep(1)
	        GPIO.cleanup()
	    except KeyboardInterrupt:
	        GPIO.cleanup()
		
	return 'Turn Off Success!'

@app.route('/tvon')
def tvon():
	os.system('irsend SEND_ONCE TV KEY_POWER')
	time.sleep(2)

	return 'TV On Successfully'

@app.route('/tvoff')
def tvoff():
	os.system('irsend SEND_ONCE TV KEY_POWER')
	time.sleep(2)

	return 'TV Off Successfully'


@app.route('/wired')
def wired():
	os.system('irsend SEND_ONCE TV KEY_AUX')
	time.sleep(3)
	os.system('irsend SEND_ONCE TV KEY_AUX')
	time.sleep(3)
	os.system('irsend SEND_ONCE TV KEY_AUX')
	time.sleep(3)
	os.system('irsend SEND_ONCE TV KEY_OK')
	time.sleep(3)
	os.system('irsend SEND_ONCE TV KEY_EXIT')
	time.sleep(1)

	return 'TV Wired Mode'

@app.route('/wireless')
def wireless():
	os.system('irsend SEND_ONCE TV KEY_AUX')
	time.sleep(3)
	os.system('irsend SEND_ONCE TV KEY_AUX')
	time.sleep(3)
	os.system('irsend SEND_ONCE TV KEY_AUX')
	time.sleep(3)
	os.system('irsend SEND_ONCE TV KEY_AUX')
	time.sleep(3)
	os.system('irsend SEND_ONCE TV KEY_OK')
	time.sleep(3)
	os.system('irsend SEND_ONCE TV KEY_EXIT')
	time.sleep(1)

	return 'TV Wired Mode'


@app.route('/projector')
def projector():
	os.system('irsend SEND_ONCE PROJECTOR KEY_POWER')
	time.sleep(3)
	os.system('irsend SEND_ONCE PROJECTOR KEY_POWER')
	time.sleep(2)
	return 'Projector turned on'


@app.route('/screendown')
def screeendown():
	turun = 19
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(turun, GPIO.OUT)
	
	#down
	def motor_on(pin):
	    GPIO.output(pin, GPIO.HIGH)  # Turn motor on
	
	def motor_off(pin):
	    GPIO.output(pin, GPIO.LOW)  # Turn motor off
	
	if __name__ == '__main__':
	    try:
	        motor_on(turun)
	        time.sleep(1)
	        motor_off(turun)
	        time.sleep(1)
	        motor_on(turun)
	        time.sleep(1)
	        motor_off(turun)
	        time.sleep(1)
	        GPIO.cleanup()
	    except KeyboardInterrupt:
	        GPIO.cleanup()
	return 'Screen projector successfully down'

@app.route('/screenup')
def screeenup():
	naik = 6
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(naik, GPIO.OUT)
	
	#up
	def motor_on(pin):
	    GPIO.output(pin, GPIO.HIGH)  # Turn motor on
	
	def motor_off(pin):
	    GPIO.output(pin, GPIO.LOW)  # Turn motor off
	
	if __name__ == '__main__':
	    try:
	        motor_on(naik)
	        time.sleep(1)
	        motor_off(naik)
	        time.sleep(1)
	        motor_on(naik)
	        time.sleep(1)
	        motor_off(naik)
	        time.sleep(1)
	        GPIO.cleanup()
	    except KeyboardInterrupt:
	        GPIO.cleanup()

	return 'Screen projector successfully up'


@app.route('/test')
def test():
	return 'Test hello world'

if __name__ == '__main__':
    app.run(debug=True, port=8181, host='0.0.0.0')

