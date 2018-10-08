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
'''

# TODO: at some point, this file could be represented as a YAML and dynamically loaded into the
# program at run time, since there are only 2 or 3 such files in the forseeable future,
# I will keep this in code. also there is only 1 pathway that gets executed everytime so I
# am confident there are not bugs in the compute files

class Pi3b(BaseCompute):
    def __init__(self):
        super().__init__()

        # Pin Layout
        self.pin_layout = [list(range(1, 40, 2)), list(range(2, 41, 2))]

        # Pin Map
        self.pins = []
        self.pins.append(ComputePin(name = "DC_POWER_3_3V_01",  pin_number = 1,  tags = [ComputePinTag.POWER, ComputePinTag.POWER_3_3]))
        self.pins.append(ComputePin(name = "DC_POWER_5V_02",    pin_number = 2,  tags = [ComputePinTag.POWER, ComputePinTag.POWER_5]))
        self.pins.append(ComputePin(name = "GPIO_02",           pin_number = 3,  tags = [ComputePinTag.GPIO],         gpio_pin = 2))
        self.pins.append(ComputePin(name = "DC_POWER_5V_04",    pin_number = 4,  tags = [ComputePinTag.POWER, ComputePinTag.POWER_5]))
        self.pins.append(ComputePin(name = "GPIO_03",           pin_number = 5,  tags = [ComputePinTag.GPIO],         gpio_pin = 3))
        self.pins.append(ComputePin(name = "GROUND_06",         pin_number = 6,  tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_04",           pin_number = 7,  tags = [ComputePinTag.GPIO],         gpio_pin = 4))
        self.pins.append(ComputePin(name = "GPIO_14",           pin_number = 8,  tags = [ComputePinTag.GPIO],         gpio_pin = 14))
        self.pins.append(ComputePin(name = "GROUND_09",         pin_number = 9,  tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_15",           pin_number = 10, tags = [ComputePinTag.GPIO],         gpio_pin = 15))
        self.pins.append(ComputePin(name = "GPIO_17",           pin_number = 11, tags = [ComputePinTag.GPIO],         gpio_pin = 17))
        self.pins.append(ComputePin(name = "GPIO_18",           pin_number = 12, tags = [ComputePinTag.GPIO],         gpio_pin = 18))
        self.pins.append(ComputePin(name = "GPIO_27",           pin_number = 13, tags = [ComputePinTag.GPIO],         gpio_pin = 27))
        self.pins.append(ComputePin(name = "GROUND_14",         pin_number = 14, tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_22",           pin_number = 15, tags = [ComputePinTag.GPIO],         gpio_pin = 22))
        self.pins.append(ComputePin(name = "GPIO_23",           pin_number = 16, tags = [ComputePinTag.GPIO],         gpio_pin = 23))
        self.pins.append(ComputePin(name = "DC_POWER_3_3V_17",  pin_number = 17, tags = [ComputePinTag.POWER, ComputePinTag.POWER_3_3]))
        self.pins.append(ComputePin(name = "GPIO_24",           pin_number = 18, tags = [ComputePinTag.GPIO],         gpio_pin = 24))
        self.pins.append(ComputePin(name = "GPIO_10",           pin_number = 19, tags = [ComputePinTag.GPIO],         gpio_pin = 10))
        self.pins.append(ComputePin(name = "GROUND_20",         pin_number = 20, tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_09",           pin_number = 21, tags = [ComputePinTag.GPIO],         gpio_pin = 9))
        self.pins.append(ComputePin(name = "GPIO_25",           pin_number = 22, tags = [ComputePinTag.GPIO],         gpio_pin = 25))
        self.pins.append(ComputePin(name = "GPIO_11",           pin_number = 23, tags = [ComputePinTag.GPIO],         gpio_pin = 11))
        self.pins.append(ComputePin(name = "GPIO_08",           pin_number = 24, tags = [ComputePinTag.GPIO],         gpio_pin = 8))
        self.pins.append(ComputePin(name = "GROUND_25",         pin_number = 25, tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_07",           pin_number = 26, tags = [ComputePinTag.GPIO],         gpio_pin = 7))
        self.pins.append(ComputePin(name = "ID_SD",             pin_number = 27, tags = [ComputePinTag.RESERVED]))
        self.pins.append(ComputePin(name = "ID_SC",             pin_number = 28, tags = [ComputePinTag.RESERVED]))
        self.pins.append(ComputePin(name = "GPIO_05",           pin_number = 29, tags = [ComputePinTag.GPIO],         gpio_pin = 5))
        self.pins.append(ComputePin(name = "GROUND_30",         pin_number = 30, tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_06",           pin_number = 31, tags = [ComputePinTag.GPIO],         gpio_pin = 6))
        self.pins.append(ComputePin(name = "GPIO_12",           pin_number = 32, tags = [ComputePinTag.GPIO],         gpio_pin = 12))
        self.pins.append(ComputePin(name = "GPIO_13",           pin_number = 33, tags = [ComputePinTag.GPIO],         gpio_pin = 13))
        self.pins.append(ComputePin(name = "GROUND_34",         pin_number = 34, tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_19",           pin_number = 35, tags = [ComputePinTag.GPIO],         gpio_pin = 19))
        self.pins.append(ComputePin(name = "GPIO_16",           pin_number = 36, tags = [ComputePinTag.GPIO],         gpio_pin = 16))
        self.pins.append(ComputePin(name = "GPIO_26",           pin_number = 37, tags = [ComputePinTag.GPIO],         gpio_pin = 26))
        self.pins.append(ComputePin(name = "GPIO_20",           pin_number = 38, tags = [ComputePinTag.GPIO],         gpio_pin = 20))
        self.pins.append(ComputePin(name = "GROUND_39",         pin_number = 39, tags = [ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name = "GPIO_21",           pin_number = 40, tags = [ComputePinTag.GPIO],         gpio_pin = 21))

    def getPins(self):
        return self.pins

    def getLayout(self):
        return self.pin_layout
