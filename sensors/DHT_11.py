#!/usr/bin/python

from BaseSensor import BaseSensor

# import Adafruit_DHT
import pdb


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

# class SensorPins(Enum):
#     POWER = 1
#     GROUND = 2

class DHT_11(BaseSensor):
    def __init__(self):
        super().__init__()

        # self.sensor = Adafruit_DHT.DHT11
        self.PIN__POWER = None
        self.PIN__GROUND = None
        self.PIN__SIGNAL = None
        self.DATA__temperature = None
        self.DATA__humidity = None

        # TODO:
        # ad events here

    # def validPinNames(self):
    #     return ["POWER", "GROUND", "SIGNAL"]
    #
    # def validDataElementNames(self):
    #     return ["temperature", "humidity"]
    #
    # def validEventElementNames(self):
    #     return ["TEMPERATURE_EXCEEDED_ROOM_TEMPERATURE", "HUMIDITY_DROPPED_BELOW_50"]

    def configure(self):


        print ("configuring sensor")
        # Check if pins are valid
        # TODO: implement these
        # self.pinMustHaveOneOfTheseTags(sensorPinName = "POWER", tags = [ComputePinTag.POWER_5])
        # self.pinMustHaveOneOfTheseTags(sensorPinName = "GROUND", tags = [ComputePinTag.GROUND])
        # self.pinMustHaveOneOfTheseTags(sensorPinName = "SIGNAL", tags = [ComputePinTag.GPIO])

        # Set input pin
        # self.gpioPinNumber = self.getPinNumber("SIGNAL")
        # self.PIN__GROUND = 2
        # print ("pin number: " + pinNumber)


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

        # self.DATA__humidity, self.DATA__temperature = Adafruit_DHT.read(self.sensor, self.PIN__SIGNAL)


    def clean(self):
        # print ("select the requested elements, convert to correct units and create a dict object that can be added to the final json. please think of a better name")
        # TODO: based on the flags that are set, create a dict containing
        # data in correct format

        # TODO: format self.DATA__temperature and self.DATA__humidity here
        # TODO: body optional
        # self.DATA__temperature = int()

        # response = {}
        # if "temperature" in self.dataElements:
        #     response["temperature"] = self.temperature
        # if "humidity" in self.dataElements:
        #     response["humidity"] = self.humidity

        return response
