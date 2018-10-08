#!/usr/bin/python

import pdb
from enum import Enum
import os
import yaml

class SensorPin:
    def __init__(self, name):
        self.name = name

class ComputePin:
    def __init__(self, name, pin_number, tags, gpio_pin = None):
        self.name = name
        self.pin_number = pin_number
        self.tags = tags
        self.gpio_pin = gpio_pin


class PinConnection:
    def __init__(self, sensor_pin, compute_pin):
        self.sensor_pin = sensor_pin
        self.compute_pin = compute_pin

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

def failSensorConfiguration(sensor, message):
    print ("Unable to configure sensor: " + sensor.name + ", \nError: " + message)
    exit()

def failEventConfiguration(event, message):
    print ("Unable to configure event: " + str(event.PARAM__info) + ", \nError: " + message)
    exit()

def loadConfiguration(config_file_path, params):
    print ("Loading config file: " + config_file_path)
    # Extract config data from config file
    if not os.path.exists(config_file_path):
        fail("Error: config file does not exist")

    # Read file and parse as yaml
    config = yaml.load(open(config_file_path))

    # Check for elements in the config file
    for param in params:
        if param not in config:
            fail("Error: " + param + " missing in config file")

    configurations = []
    for param in params:
        configurations.append(config[param])
    return configurations


def importClassDynamically(class_name):
    try:
        components = class_name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return getattr(mod, class_name)()
    except Exception as e:
        fail ("Error: Exception occurred while trying to load class: " + class_name + \
              "\nException: " + str(e))

def createClassLevelObjects(class_object, prefix, variable_list):
    for variable in variable_list:
        setattr(class_object, prefix + variable, None)
