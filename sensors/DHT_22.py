from sensors.BaseSensor import BaseSensor
from scripts.helper.common import fail, failSensorConfiguration, ComputePinTag
# TODO: install Adafruit library for DHT11/DHT22 first and than uncomment the following line
# import Adafruit_DHT


class DHT_22(BaseSensor):
    def __init__(self):
        super().__init__()

        # define native variables
        self.current_humidity = None
        self.current_temperature = None
        self.sensor_model = None
        self.temp_unit = None
        self.signal_pin = None

    def __temp_unit_change(self):
        if self.temp_unit == 'C':
            return self.current_humidity, self.current_temperature
        elif self.temp_unit == 'F':
            self.current_temperature = (self.current_temperature * (9 / 5)) + 32
            return self.current_humidity, self.current_temperature
        else:
            self.current_temperature = self.current_temperature + 273.15
            return self.current_humidity, self.current_temperature

    def listPins(self):
        return ['POWER', 'GROUND', 'SIGNAL']

    def listSignals(self):
        return ['temperature', 'humidity']

    def listParameters(self):
        return ['model', 'temp_unit']

    def configure(self):
        #TODO: understand the configuration checks and than implement that
        self.sensor_model = self.model
        self.temp_unit = self.temp_unit
        self.signal_pin = self.PIN__SIGNAL.gpioPin

    def update(self):
        self.current_temperature, self.current_humidity = Adafruit_DHT.read_retry(self.sensor_model, self.signal_pin)

    def report(self):
        self.temperature, self.humidity = self.__temp_unit_change()

    def afterReport(self):
        pass
