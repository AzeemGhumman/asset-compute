#!/usr/bin/python

from BaseSensor import BaseSensor

# import Adafruit_DHT
import pdb
import sys
# Load common
sys.path.append('../scripts/helper/')
from common import fail, failSensorConfiguration, ComputePinTag

class DHT(BaseSensor):
    def __init__(self):
        super().__init__()
        self.current_humidity = None
        self.current_temperature = None

    def listPins(self):
        return ["POWER", "GROUND", "SIGNAL"]

    def listSignals(self):
        return ["temperature", "humidity"]

    def listParameters(self):
        return ["model", "temperature_unit", "humidity_unit"]

    def configure(self):
        if ComputePinTag.POWER_5 not in self.PIN__POWER.tags:
            failSensorConfiguration (self, "Power not connected properly")
        if ComputePinTag.GROUND not in self.PIN__GROUND.tags:
            failSensorConfiguration (self, "Ground not connected properly")
        if ComputePinTag.GPIO not in self.PIN__SIGNAL.tags:
            failSensorConfiguration (self, "SIGNAL pin must be connected to a GPIO pin")
        # TODO: check model, complain if not set when using the same DHT class for both models 11 and 22

        '''
        if PARAM__model is 11:
            self.sensor = Adafruit_DHT.DHT11
        elif PARAM__model is 22:
            self.sensor = Adafruit_DHT.DHT22
        else:
            failSensorConfiguration (self, "Invalid Model number")
        '''

    def update(self):
        # self.current_humidity, self.current_temperature = Adafruit_DHT.read(self.sensor, self.PIN__SIGNAL.gpioPin)
        pass

    def report(self):
        self.temperature = {"value" : self.current_humidity}
        self.humidity = {"value" : self.current_temperature}

    def afterReport(self):
        pass
