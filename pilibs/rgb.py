import RPi.GPIO as GPIO


class RGB(object):
    RED = 19
    GREEN = 26
    BLUE = 13

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RED, GPIO.OUT)
        GPIO.setup(self.GREEN, GPIO.OUT)
        GPIO.setup(self.BLUE, GPIO.OUT)

    def red(self):
        GPIO.output(self.RED, 1),
        GPIO.output(self.GREEN, 0),
        GPIO.output(self.BLUE, 0),
        return True

    def green(self):
        GPIO.output(self.RED, 0),
        GPIO.output(self.GREEN, 1),
        GPIO.output(self.BLUE, 0),
        return True

    def blue(self):
        GPIO.output(self.RED, 0),
        GPIO.output(self.GREEN, 0),
        GPIO.output(self.BLUE, 1),
        return True

    def destroy(self):
        GPIO.output(self.RED, 0),
        GPIO.output(self.GREEN, 0),
        GPIO.output(self.BLUE, 0),
        return True

    @classmethod
    def cleanup(cls):
        GPIO.cleanup()
