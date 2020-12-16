import RPi.GPIO as GPIO
import time

DEFAULT_SPEED = 50
FREQUENCY = 10 # Hz

class Motor:
	def __init__(self, in1Pin, in2Pin, pwmPin, offset, stbyPin, mode=GPIO.BCM):
		GPIO.setmode(mode)
		self.in1 = in1Pin
		self.in2 = in2Pin,
		self.pwm = pwmPin
		self.standbyPin = stbyPin
		
		if offset == -1:
			self.offset = -1
		else:
			self.offset = 1
		
		GPIO.setup(self.in1, GPIO.OUT)
		GPIO.setup(self.in2, GPIO.OUT)
		GPIO.setup(self.pwm, GPIO.OUT)
		GPIO.setup(self.standbyPin, GPIO.OUT)
		
		self.speed = GPIO.PWM(self.pwm, FREQUENCY)
		self.speed.start(0)
	
	def drive(self, speed, duration=None):
		GPIO.output(self.standbyPin, GPIO.HIGH)
		speed = speed * self.offset;
		if speed >= 0:
			self._fwd(speed)
		else:
			self._rev(-speed)
		if duration:
			time.sleep(duration)
			
		
	def brake(self):
		GPIO.output(self.in1, GPIO.HIGH)
		GPIO.output(self.in2, GPIO.HIGH)
		self.speed.ChangeDutyCycle(0)
		
	def standby(self):
		GPIO.output(self.standbyPin, GPIO.LOW)
		
	def _fwd(self, speed):
		GPIO.output(self.in1, GPIO.HIGH)
		GPIO.output(self.in2, GPIO.LOW)
		self.speed.ChangeDutyCycle(speed)
		
	def _rev(self, speed):
		GPIO.output(self.in1, GPIO.LOW)
		GPIO.output(self.in2, GPIO.HIGH)
		self.speed.ChangeDutyCycle(speed)
		
	def __del__(self):
		self.standby()
		self.speed.stop()
		
		
def forward(motor1, motor2, speed=DEFAULT_SPEED):
	if isinstance(motor1, Motor) and isinstance(motor2, Motor):
		motor1.drive(speed)
		motor2.drive(speed)


def backward(motor1, motor2, speed=DEFAULT_SPEED):
	if isinstance(motor1, Motor) and isinstance(motor2, Motor):
		temp = abs(speed)
		motor1.drive(-temp)
		motor2.drive(-temp)


def left(leftMotor, rightMotor, speed=DEFAULT_SPEED):
	if isinstance(motor1, Motor) and isinstance(motor2, Motor):
		temp = abs(speed)/2
		leftMotor.drive(-temp)
		rightMotor.drive(temp)
		
	
def right(leftMotor, rightMotor, speed=DEFAULT_SPEED):
	if isinstance(motor1, Motor) and isinstance(motor2, Motor):
		temp = abs(speed)/2
		leftMotor.drive(temp)
		rightMotor.drive(-temp)

		
def brake(motor1, motor2, speed=DEFAULT_SPEED):
	if isinstance(motor1, Motor) and isinstance(motor2, Motor):
		motor1.brake()
		motor2.brake()
