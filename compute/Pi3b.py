#!/usr/bin/python

from BaseCompute import BaseCompute

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
        pinMap["manifestName"] = (pinNumber = X, tags = ["power", "reserved"])
'''

class Pi3b(BaseCompute):
    def __init__(self):
        super().__init__()

        # Pin Layout
        self.pinLayout = [list(range(1, 40, 2)), list(range(2, 41, 2))]

        # Pin Map
        self.pinMap = {}
        self.pinMap["DC_POWER_3_3V_01"]  = {"pinNumber" : 1,  "tags" : ["POWER_3.3V"]}
        self.pinMap["DC_POWER_5V_02"]    = {"pinNumber" : 2,  "tags" : ["POWER_5V"]}
        self.pinMap["GPIO_02"]           = {"pinNumber" : 3,  "tags" : ["GPIO"],         "gpioPin" : 2}
        self.pinMap["DC_POWER_5V_04"]    = {"pinNumber" : 4,  "tags" : ["POWER_5V"]}
        self.pinMap["GPIO_03"]           = {"pinNumber" : 5,  "tags" : ["GPIO"],         "gpioPin" : 3}
        self.pinMap["GROUND_06"]         = {"pinNumber" : 6,  "tags" : ["GROUND"]}
        self.pinMap["GPIO_04"]           = {"pinNumber" : 7,  "tags" : ["GPIO"],         "gpioPin" : 4}
        self.pinMap["GPIO_14"]           = {"pinNumber" : 8,  "tags" : ["GPIO"],         "gpioPin" : 14}
        self.pinMap["GROUND_09"]         = {"pinNumber" : 9,  "tags" : ["GROUND"]}
        self.pinMap["GPIO_15"]           = {"pinNumber" : 10, "tags" : ["GPIO"],         "gpioPin" : 15}
        self.pinMap["GPIO_17"]           = {"pinNumber" : 11, "tags" : ["GPIO"],         "gpioPin" : 17}
        self.pinMap["GPIO_18"]           = {"pinNumber" : 12, "tags" : ["GPIO"],         "gpioPin" : 18}
        self.pinMap["GPIO_27"]           = {"pinNumber" : 13, "tags" : ["GPIO"],         "gpioPin" : 27}
        self.pinMap["GROUND_14"]         = {"pinNumber" : 14, "tags" : ["GROUND"]}
        self.pinMap["GPIO_22"]           = {"pinNumber" : 15, "tags" : ["GPIO"],         "gpioPin" : 22}
        self.pinMap["GPIO_23"]           = {"pinNumber" : 16, "tags" : ["GPIO"],         "gpioPin" : 23}
        self.pinMap["DC_POWER_3_3V_17"]  = {"pinNumber" : 17, "tags" : ["POWER_3.3V"]}
        self.pinMap["GPIO_24"]           = {"pinNumber" : 18, "tags" : ["GPIO"],         "gpioPin" : 24}
        self.pinMap["GPIO_10"]           = {"pinNumber" : 19, "tags" : ["GPIO"],         "gpioPin" : 10}
        self.pinMap["GROUND_20"]         = {"pinNumber" : 20, "tags" : ["GROUND"]}
        self.pinMap["GPIO_09"]           = {"pinNumber" : 21, "tags" : ["GPIO"],         "gpioPin" : 9}
        self.pinMap["GPIO_25"]           = {"pinNumber" : 22, "tags" : ["GPIO"],         "gpioPin" : 25}
        self.pinMap["GPIO_11"]           = {"pinNumber" : 23, "tags" : ["GPIO"],         "gpioPin" : 11}
        self.pinMap["GPIO_08"]           = {"pinNumber" : 24, "tags" : ["GPIO"],         "gpioPin" : 8}
        self.pinMap["GROUND_25"]         = {"pinNumber" : 25, "tags" : ["GROUND"]}
        self.pinMap["GPIO_07"]           = {"pinNumber" : 26, "tags" : ["GPIO"],         "gpioPin" : 7}
        self.pinMap["ID_SD"]             = {"pinNumber" : 27, "tags" : ["RESERVED"]}
        self.pinMap["ID_SC"]             = {"pinNumber" : 28, "tags" : ["RESERVED"]}
        self.pinMap["GPIO_05"]           = {"pinNumber" : 29, "tags" : ["GPIO"],         "gpioPin" : 5}
        self.pinMap["GROUND_30"]         = {"pinNumber" : 30, "tags" : ["GROUND"]}
        self.pinMap["GPIO_06"]           = {"pinNumber" : 31, "tags" : ["GPIO"],         "gpioPin" : 6}
        self.pinMap["GPIO_12"]           = {"pinNumber" : 32, "tags" : ["GPIO"],         "gpioPin" : 12}
        self.pinMap["GPIO_13"]           = {"pinNumber" : 33, "tags" : ["GPIO"],         "gpioPin" : 13}
        self.pinMap["GROUND_34"]         = {"pinNumber" : 34, "tags" : ["GROUND"]}
        self.pinMap["GPIO_19"]           = {"pinNumber" : 35, "tags" : ["GPIO"],         "gpioPin" : 19}
        self.pinMap["GPIO_16"]           = {"pinNumber" : 36, "tags" : ["GPIO"],         "gpioPin" : 16}
        self.pinMap["GPIO_26"]           = {"pinNumber" : 37, "tags" : ["GPIO"],         "gpioPin" : 26}
        self.pinMap["GPIO_20"]           = {"pinNumber" : 38, "tags" : ["GPIO"],         "gpioPin" : 20}
        self.pinMap["GROUND_39"]         = {"pinNumber" : 39, "tags" : ["GROUND"]}
        self.pinMap["GPIO_21"]           = {"pinNumber" : 40, "tags" : ["GPIO"],         "gpioPin" : 21}

    def getPinMap(self):
        return self.pinMap

    def getPinLayout(self):
        return self.pinLayout
