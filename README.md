# TB6612FNG_Pi
Sparkfun TB6612FNG dual motor driver arduino library ported for Python on Raspberry PI

## Usage
1. Import the class  
```python
import SparkFun_TB6612FNG as Driver
```
2. Instantiate the Motor  
```python
motor = Driver.Motor(in1Pin, in2Pin, pwmPin, offset, standbyPin)
#offset is 1 or -1, used for lining up with names like forwards and backwards
```
3. Drive
```python
motor.drive(255)
if condition:
  motor.brake()

# Drive with delay
motor.drive(255, 4)
```
