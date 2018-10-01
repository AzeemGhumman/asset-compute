#!/usr/bin/python


print ("run main loop")
print ("expect a manifest file name as input")



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
