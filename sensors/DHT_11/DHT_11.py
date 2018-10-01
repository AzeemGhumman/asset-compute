#!/usr/bin/python

import Adafruit_DHT

'''
# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
'''


class DHT_11(BaseSensor):
    def __init__(self):
        super().__init__()

        self.sensor = Adafruit_DHT.DHT11
        self.pinGround = None
        self.pinPower = None
        self.pinData = None
        self.isReportTemperature = False
        self.isReportHumidity = False
        self.lastTemperature = None
        self.lastHumidity = None

    def configure(self, sensorConfiguration):
        print ("configuring DHT_11 sensor")

        # TODO: make assertions about where all the pins are connected.
        # TODO: for example, for ground, we can check that it is connected to
        # any valid ground, same for power. 3.3, 5, etc.

        # TODO: set pins here
        # TODO: set enable disable for types of data reported

        # TODO: return success | failure?

    def read(self):
        print ("reading data from the sensor")
        # TODO: No need to return anything. just update member variables
        # TODO: Maybe return a success | failure flag, but won't make sense in multithreaded application

        self.humidity, self.temperature = Adafruit_DHT.read(self.sensor, self.pinData)


    def clean(self):
        print ("select the requested elements, convert to correct units and create a dict object that can be added to the final json. please think of a better name")
        # TODO: based on the flags that are set, create a dict containing
        # data in correct format
        return {}
