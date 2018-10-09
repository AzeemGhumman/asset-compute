#!/usr/bin/python

import yaml
import os
import pdb
import sys
from time import sleep

'''
TODO: We might want to run the read() method of each sensor
 at a different rate than the specified rate. This will give
 us more granular data that might be used to detect events that require
 granular data. We can make a distinction between read() that updates the
 output and read that updates the internal state of the sensor objects
 we can define 2 different rates in the manifest for each sensor
'''

# Load compute
sys.path.append('../compute/')
import BaseCompute

# Load sensors
sys.path.append('../sensors/')
import BaseSensor

# Load events
sys.path.append('../events/')
import BaseEvent

# Load common
sys.path.append('../scripts/helper/')
from common import SensorPin, ComputePin, PinConnection
from common import fail, loadConfiguration, importClassDynamically

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

if len(sys.argv) < 2:
    fail ("Error: Manifest file path required")
# manifest_file_path = "../manifests/device-13.yaml"
manifest_file_path = sys.argv[1]

param_device_name, param_hardware_type, param_queue_size, param_sensors, param_events, param_output = \
    loadConfiguration(config_file_path = manifest_file_path, \
    params = ["device-name", "hardware-type", 'queue-size', "sensors", "events", "output"])

# Dynamically load the compute class
compute_class = importClassDynamically(param_hardware_type)


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
str_sensor_name = "name"
str_sensor_type = "type"
str_sensor_signal_elements = "signals"
str_sensor_connections = "connections"
str_sensor_connection_compute = "compute"
str_sensor_connection_sensor = "sensor"
str_events = "events"
str_event_type = "type"
str_sensor_parameters = "params"


# TODO: create method read manifest and load an object that represents the manifest
# update validate code so that it loads, configures and reads once data from all sensors

# Store sensor objects in a list
sensors = {}

for sensor in param_sensors:

    # Check if a sensor attribute is missing
    # TODO: Check if attributes bessides connections are missing
    if str_sensor_connections not in sensor:
        fail ("Error: Connection is missing for sensor: " + sensor[str_sensor_name])

    # Fail if sensor name is repeated
    if sensor[str_sensor_name] in sensors:
        fail("Error: Sensor names must be unique. Duplicate sensor: " + sensor[str_sensor_name])

    # Update conncetions: get pinMap from pin name for each compute pin
    connections = []
    for connection in sensor[str_sensor_connections]:
        sensor_pin = SensorPin(name = connection[str_sensor_connection_sensor])
        compute_pin_name = connection[str_sensor_connection_compute]
        compute_pin = compute_class.getPin(compute_pin_name)
        if compute_pin is None:
            fail ("Pin: " + str(compute_pin) + " not found in selected compute")
        connections.append(PinConnection(sensor_pin, compute_pin))

    sensorObject = importClassDynamically(sensor[str_sensor_type])

    sensorObject.setSensorConfigurations(name = sensor[str_sensor_name], \
                                        signal_elements = sensor[str_sensor_signal_elements], \
                                        connections = connections, \
                                        params = sensor[str_sensor_parameters])

    sensors[sensor[str_sensor_name]] = sensorObject

# Configure events
events = []
for event in param_events:

    event_type = event[str_event_type]
    eventObject = importClassDynamically(event_type)
    eventObject.configureEvent(type = event_type, event_dict = event, sensors_data = sensors)
    events.append(eventObject)

# Check for duplicate events
event_set = set()
for event in events:
    if event.PARAM__name in event_set:
        fail ("Error: Event names must be unique. Duplicate event: " + event.PARAM__name)
    event_set.add(event.PARAM__name)

print ("all sensors have been configured")
# All sensors have been configured

counter = 0
while True:
    output = {}
    for sensor_name, sensor in sensors.items():
        sensor.update()
        print ("reading sensor data...")
        output[sensor.name] = sensor.writeData(events_data = events)
    print (output)
    sleep(1)
    counter += 1
    # TODO: add timestamp and device id and create yaml and send to end point


'''
every time unit:
    create list of sensors that need to be read this time
    create a separate thread for each sensor or a thread pool
    wait until all threads are finished
    create a json object from the output of all the responses
'''


# pdb.set_trace()
