#!/usr/bin/python

from BaseCompute import BaseCompute

import sys
# Load common code
sys.path.append('../scripts/helper/')
from common import ComputePin, ComputePinTag

'''
Assumption:
    - Same code can run on different types of Raspberry PIs
    The rationale for creating different 'types' of compute is to capture the pinout
    Since we heavily depend on external code for low-level drivers that is specifically
    written for BBB or Raspberry PI, I dont see the need to maintain separate code
    for each type of board.

    PinOut is captured here.
    This helps in creating a readable manifest
    Also, we can add tags with each pin, e.g., GND, VCC-3, VCC-5, GPIO, other, etc.
    This mapping allows the sensors to check if the connections are made correctly
    when configuring the hardware on startup.
    e.g, a sensors can check if the GND, power and signal pin is connected to valid
    pins on the actual board.

    class PI_3:
        pin number: 23
        name: GPIO_32 (shows up in manifest)
        tags: [GPIO, reserved]

        a map!
        pins["manifestName"] = (pinNumber = X, tags = ["power", "reserved"])
'''

# TODO: at some point, this file could be represented as a YAML and dynamically loaded into the
# program at run time, since there are only 2 or 3 such files in the forseeable future,
# I will keep this in code. also there is only 1 pathway that gets executed everytime so I
# am confident there are not bugs in the compute files

class Pi3b(BaseCompute):
    def __init__(self):
        super().__init__()

        # Pin Layout
        self.pinLayout = [list(range(1, 40, 2)), list(range(2, 41, 2))]

        # Pin Map
        self.pins = []
        self.pins.append(ComputePin(name = "DC_POWER_3_3V_01",  pinNumber = 1,  tags = [ComputePinTag.POWER, ComputePinTag.POWER_3_3]))
        self.pins.append(ComputePin(name = "DC_POWER_5V_02",    pinNumber = 2,  tags = [ComputePinTag.POWER, ComputePinTag.POWER_5]))
        self.pins.append(ComputePin(name = "GPIO_02",           pinNumber = 3,  tags = [ComputePinTag.GPIO],         gpioPin = 2))
        self.pins.append(ComputePin(name = "DC_POWER_5V_04",    pinNumber = 4,  tags = [ComputePinTag.POWER, ComputePinTag.POWER_5]))
        self.pins.append(ComputePin(name = "GPIO_03",           pinNumber = 5,  tags = [ComputePinTag.GPIO],         gpioPin = 3))
        self.pins.append(ComputePin(name = "GROUND_06",         pinNumber = 6,  tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_04",           pinNumber = 7,  tags = [ComputePinTag.GPIO],         gpioPin = 4))
        self.pins.append(ComputePin(name = "GPIO_14",           pinNumber = 8,  tags = [ComputePinTag.GPIO],         gpioPin = 14))
        self.pins.append(ComputePin(name = "GROUND_09",         pinNumber = 9,  tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_15",           pinNumber = 10, tags = [ComputePinTag.GPIO],         gpioPin = 15))
        self.pins.append(ComputePin(name = "GPIO_17",           pinNumber = 11, tags = [ComputePinTag.GPIO],         gpioPin = 17))
        self.pins.append(ComputePin(name = "GPIO_18",           pinNumber = 12, tags = [ComputePinTag.GPIO],         gpioPin = 18))
        self.pins.append(ComputePin(name = "GPIO_27",           pinNumber = 13, tags = [ComputePinTag.GPIO],         gpioPin = 27))
        self.pins.append(ComputePin(name = "GROUND_14",         pinNumber = 14, tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_22",           pinNumber = 15, tags = [ComputePinTag.GPIO],         gpioPin = 22))
        self.pins.append(ComputePin(name = "GPIO_23",           pinNumber = 16, tags = [ComputePinTag.GPIO],         gpioPin = 23))
        self.pins.append(ComputePin(name = "DC_POWER_3_3V_17",  pinNumber = 17, tags = [ComputePinTag.POWER, ComputePinTag.POWER_3_3]))
        self.pins.append(ComputePin(name = "GPIO_24",           pinNumber = 18, tags = [ComputePinTag.GPIO],         gpioPin = 24))
        self.pins.append(ComputePin(name = "GPIO_10",           pinNumber = 19, tags = [ComputePinTag.GPIO],         gpioPin = 10))
        self.pins.append(ComputePin(name = "GROUND_20",         pinNumber = 20, tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_09",           pinNumber = 21, tags = [ComputePinTag.GPIO],         gpioPin = 9))
        self.pins.append(ComputePin(name = "GPIO_25",           pinNumber = 22, tags = [ComputePinTag.GPIO],         gpioPin = 25))
        self.pins.append(ComputePin(name = "GPIO_11",           pinNumber = 23, tags = [ComputePinTag.GPIO],         gpioPin = 11))
        self.pins.append(ComputePin(name = "GPIO_08",           pinNumber = 24, tags = [ComputePinTag.GPIO],         gpioPin = 8))
        self.pins.append(ComputePin(name = "GROUND_25",         pinNumber = 25, tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_07",           pinNumber = 26, tags = [ComputePinTag.GPIO],         gpioPin = 7))
        self.pins.append(ComputePin(name = "ID_SD",             pinNumber = 27, tags = [ComputePinTag.RESERVED]))
        self.pins.append(ComputePin(name = "ID_SC",             pinNumber = 28, tags = [ComputePinTag.RESERVED]))
        self.pins.append(ComputePin(name = "GPIO_05",           pinNumber = 29, tags = [ComputePinTag.GPIO],         gpioPin = 5))
        self.pins.append(ComputePin(name = "GROUND_30",         pinNumber = 30, tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_06",           pinNumber = 31, tags = [ComputePinTag.GPIO],         gpioPin = 6))
        self.pins.append(ComputePin(name = "GPIO_12",           pinNumber = 32, tags = [ComputePinTag.GPIO],         gpioPin = 12))
        self.pins.append(ComputePin(name = "GPIO_13",           pinNumber = 33, tags = [ComputePinTag.GPIO],         gpioPin = 13))
        self.pins.append(ComputePin(name = "GROUND_34",         pinNumber = 34, tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_19",           pinNumber = 35, tags = [ComputePinTag.GPIO],         gpioPin = 19))
        self.pins.append(ComputePin(name = "GPIO_16",           pinNumber = 36, tags = [ComputePinTag.GPIO],         gpioPin = 16))
        self.pins.append(ComputePin(name = "GPIO_26",           pinNumber = 37, tags = [ComputePinTag.GPIO],         gpioPin = 26))
        self.pins.append(ComputePin(name = "GPIO_20",           pinNumber = 38, tags = [ComputePinTag.GPIO],         gpioPin = 20))
        self.pins.append(ComputePin(name = "GROUND_39",         pinNumber = 39, tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_21",           pinNumber = 40, tags = [ComputePinTag.GPIO],         gpioPin = 21))

    def getPins(self):
        return self.pins

    def getLayout(self):
        return self.pinLayout
