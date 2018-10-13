from sensors.BaseSensor import BaseSensor
import RPi.GPIO as GPIO


class SW_420(BaseSensor):
    def __init__(self):
        super().__init__()

        # define native variables
        self.signal_pin = None
        self.bounce_time = None

    def listPins(self):
        return {'POWER', 'GROUND', 'SIGNAL'}

    def listSignals(self):
        return ['EVENT_DETECTED']

    def listParameters(self):
        return ['BOUNCETIME']

    def configure(self):
        # TODO: understand the configuration checks and than implement that
        self.signal_pin = self.PIN__SIGNAL.gpioPin
        self.bounce_time = self.BOUNCETIME

        GPIO.setmode(GPIO.getmode())
        GPIO.setup(self.signal_pin, GPIO.IN)

        GPIO.add_event_detect(self.signal_pin, GPIO.BOTH, bouncetime=self.bounce_time)
        GPIO.add_event_callback(self.signal_pin, self.update())

    def update(self):
        pass

    def report(self):
        pass

    def afterReport(self):
        pass



