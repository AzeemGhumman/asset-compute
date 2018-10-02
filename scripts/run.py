#!/usr/bin/python


import yaml
import os
import pdb
import sys

# Load compute
sys.path.append('../compute/')
import BaseCompute

# Load sensors
sys.path.append('../sensors/')
import BaseSensor


'''
Read yaml file
Set compute level parameters
For each sensor connceted:
    Create an object
    Configure sensor

Forever:
For each unit of time passed:
    Check if we want to read from a sensor
    For each sensor we want to read:
        Call read() for sensor
        Call parse() for each sensor
    Generate a complete JSON packet with all the sensor data, device ID and timestamp information
    Send data to REST API
    If not successful:
        If size of queue, exceeds max size:
            Drop first messages
        Add json pack to queue
'''

def fail(message):
    print (message)
    exit()

def loadConfiguration(configFilePath, params):
    print ("Loading config file: " + configFilePath)
    # Extract config data from config file
    if not os.path.exists(configFilePath):
        fail("Error: config file does not exist")

    # Read file and parse as yaml
    config = yaml.load(open(configFilePath))

    # Check for elements in the config file
    for param in params:
        if param not in config:
            fail("Error: " + param + " missing in config file")

    configurations = []
    for param in params:
        configurations.append(config[param])
    return configurations


def importClassDynamically(className):
    try:
        components = className.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return getattr(mod, className)()
    except Exception as e:
        fail ("Error: Exception occurred while trying to load class: " + className + \
              "\nException: " + str(e))

manifestFilePath = "../manifests/device-40.yaml"

paramDeviceName, paramHardwareType, paramQueueSize, paramSensors = \
    loadConfiguration(configFilePath = manifestFilePath, \
    params = ["device-name", "hardware-type", 'queue-size', "sensors"])

# print ("hardware-type: " + paramHardwareType)

# Dynamically load the compute class
computeClass = importClassDynamically(paramHardwareType)

# Load the pin map for the selected compute
computePinMap = computeClass.getPinMap()


'''
For each sensor:
    create a sensor object of the right class
    pass name, data, events, connections
    run configure()

copy everything up to this point and put in validate and expose a function

Every N seconds:
    For each sensor:
        read()
        generateOutput()
'''

# Strings used in yaml file
strSensorName = "name"
strSensorType = "type"
strSensorDataElements = "data"
strSensorEventElements = "events"
strSensorConnections = "connections"
strSensorConnectionCompute = "compute"
strSensorConnectionSense = "sense"

# Store sensor objects in a list
sensors = []

for sensor in paramSensors:
    sensorClass = importClassDynamically(sensor[strSensorType])

    # Update conncetions: get pinMap from pin name for each compute pin
    connections = []
    for connection in sensor[strSensorConnections]:
        computePin = connection[strSensorConnectionCompute]
        sensePin = connection[strSensorConnectionSense]
        if computePin not in computePinMap:
            fail ("Pin: " + str(computePin) + " not found in selected compute")
        connections.append({strSensorConnectionCompute : computePinMap[computePin], \
                            strSensorConnectionSense : sensePin})

    sensorClass.setSensorConfigurations(name = sensor[strSensorName], \
                                        dataElements = sensor[strSensorDataElements], \
                                        eventElements = sensor[strSensorEventElements], \
                                        connections = connections)
    # TODO: here

    sensorClass.configure()

    # print (sensorClass.name)

    # TODO: remove break
    break





# pdb.set_trace()
