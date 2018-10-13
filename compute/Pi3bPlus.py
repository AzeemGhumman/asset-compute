from compute import BaseCompute
from scripts.helper.common import ComputePin, ComputePinTag

'''
Introduction:
    This file includes PinNames, PinNumber for Raspberry Pi 3 model B+.
    This file is in accordance to the base class written 'BaseCompute.py'
    
'''

asset_total_pin = 40


class Pi3bPlus(BaseCompute.BaseCompute):
    def __init__(self):
        super().__init__()

        # Pin Layout
        self.pin_layout = [list(range(1, asset_total_pin, 2)), list(range(2, asset_total_pin, 2))]

        # Pin Map
        self.pins = []
        self.pins.append(ComputePin(name='DC_POWER_3_3V_01', pin_number=1, tags=[ComputePinTag.POWER, ComputePinTag.POWER_3_3]))
        self.pins.append(ComputePin(name="DC_POWER_5V_02", pin_number=2, tags=[ComputePinTag.POWER, ComputePinTag.POWER_5]))
        self.pins.append(ComputePin(name="GPIO_02", pin_number=3, tags=[ComputePinTag.GPIO], gpio_pin=2))
        self.pins.append(ComputePin(name="DC_POWER_5V_04", pin_number=4, tags=[ComputePinTag.POWER, ComputePinTag.POWER_5]))
        self.pins.append(ComputePin(name="GPIO_03", pin_number=5, tags=[ComputePinTag.GPIO], gpio_pin=3))
        self.pins.append(ComputePin(name="GROUND_06", pin_number=6, tags=[ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name="GPIO_04", pin_number=7, tags=[ComputePinTag.GPIO], gpio_pin=4))
        self.pins.append(ComputePin(name="GPIO_14", pin_number=8, tags=[ComputePinTag.GPIO], gpio_pin=14))
        self.pins.append(ComputePin(name="GROUND_09", pin_number=9, tags=[ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name="GPIO_15", pin_number=10, tags=[ComputePinTag.GPIO], gpio_pin=15))
        self.pins.append(ComputePin(name="GPIO_17", pin_number=11, tags=[ComputePinTag.GPIO], gpio_pin=17))
        self.pins.append(ComputePin(name="GPIO_18", pin_number=12, tags=[ComputePinTag.GPIO], gpio_pin=18))
        self.pins.append(ComputePin(name="GPIO_27", pin_number=13, tags=[ComputePinTag.GPIO], gpio_pin=27))
        self.pins.append(ComputePin(name="GROUND_14", pin_number=14, tags=[ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name="GPIO_22", pin_number=15, tags=[ComputePinTag.GPIO], gpio_pin=22))
        self.pins.append(ComputePin(name="GPIO_23", pin_number=16, tags=[ComputePinTag.GPIO], gpio_pin=23))
        self.pins.append(ComputePin(name="DC_POWER_3_3V_17", pin_number=17, tags=[ComputePinTag.POWER, ComputePinTag.POWER_3_3]))
        self.pins.append(ComputePin(name="GPIO_24", pin_number=18, tags=[ComputePinTag.GPIO], gpio_pin=24))
        self.pins.append(ComputePin(name="GPIO_10", pin_number=19, tags=[ComputePinTag.GPIO], gpio_pin=10))
        self.pins.append(ComputePin(name="GROUND_20", pin_number=20, tags=[ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name="GPIO_09", pin_number=21, tags=[ComputePinTag.GPIO], gpio_pin=9))
        self.pins.append(ComputePin(name="GPIO_25", pin_number=22, tags=[ComputePinTag.GPIO], gpio_pin=25))
        self.pins.append(ComputePin(name="GPIO_11", pin_number=23, tags=[ComputePinTag.GPIO], gpio_pin=11))
        self.pins.append(ComputePin(name="GPIO_08", pin_number=24, tags=[ComputePinTag.GPIO], gpio_pin=8))
        self.pins.append(ComputePin(name="GROUND_25", pin_number=25, tags=[ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name="GPIO_07", pin_number=26, tags=[ComputePinTag.GPIO], gpio_pin=7))
        self.pins.append(ComputePin(name="GPIO_0", pin_number=27, tags=[ComputePinTag.RESERVED]))
        self.pins.append(ComputePin(name="GPIO_1", pin_number=28, tags=[ComputePinTag.RESERVED]))
        self.pins.append(ComputePin(name="GPIO_05", pin_number=29, tags=[ComputePinTag.GPIO], gpio_pin=5))
        self.pins.append(ComputePin(name="GROUND_30", pin_number=30, tags=[ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name="GPIO_06", pin_number=31, tags=[ComputePinTag.GPIO], gpio_pin=6))
        self.pins.append(ComputePin(name="GPIO_12", pin_number=32, tags=[ComputePinTag.GPIO], gpio_pin=12))
        self.pins.append(ComputePin(name="GPIO_13", pin_number=33, tags=[ComputePinTag.GPIO], gpio_pin=13))
        self.pins.append(ComputePin(name="GROUND_34", pin_number=34, tags=[ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name="GPIO_19", pin_number=35, tags=[ComputePinTag.GPIO], gpio_pin=19))
        self.pins.append(ComputePin(name="GPIO_16", pin_number=36, tags=[ComputePinTag.GPIO], gpio_pin=16))
        self.pins.append(ComputePin(name="GPIO_26", pin_number=37, tags=[ComputePinTag.GPIO], gpio_pin=26))
        self.pins.append(ComputePin(name="GPIO_20", pin_number=38, tags=[ComputePinTag.GPIO], gpio_pin=20))
        self.pins.append(ComputePin(name="GROUND_39", pin_number=39, tags=[ComputePinTag.GROUND]))
        self.pins.append(ComputePin(name="GPIO_21", pin_number=40, tags=[ComputePinTag.GPIO], gpio_pin=21))

    def getLayout(self):
        return self.pin_layout

    def getPins(self):
        return self.pins
