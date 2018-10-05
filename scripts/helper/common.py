#!/usr/bin/python

import pdb
from enum import Enum

class SensorPin:
    def __init__(self, name):
        self.name = name

class ComputePin:
    def __init__(self, name, pinNumber, tags, gpioPin = None):
        self.name = name
        self.pinNumber = pinNumber
        self.tags = tags
        self.gpioPin = gpioPin


class PinConnection:
    def __init__(self, sensorPin, computePin):
        self.sensorPin = sensorPin
        self.computePin = computePin

class ComputePinTag(Enum):
    POWER_3_3 = 1
    POWER_5 = 2
    POWER = 3
    GROUND = 4
    GPIO = 5
    RESERVED = 6


def fail(message):
    print (message)
    exit()
