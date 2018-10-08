from abc import ABC, abstractmethod

import sys

# Load common
sys.path.append('../scripts/helper/')
from common import fail, failEventConfiguration, createClassLevelObjects

import pdb

class BaseEvent(ABC):

    def __init__(self):
        super().__init__()

        self.is_set = False
        self.attached_sensors = set()
        self.dynamic_objects = []
        self.suppressed_params = []
        self.sensors_data = None
        self.PARAM__type = None
        self.PARAM__name = None
        self.PARAM__info = None

    def configureEvent(self, type, event_dict, sensors_data):

        self.sensors_data = sensors_data
        prefix = "PARAM__"
        createClassLevelObjects(class_object = self, prefix = prefix, variable_list = self.listParameters())
        known_attributes = [i[len(prefix):] for i in [*vars(self)] if i.startswith(prefix)]
        for attribute in event_dict:
            if attribute not in known_attributes:
                failEventConfiguration (self, "Unknown attribute '" + str(attribute) + "' for event: " + str(type) + "'")
            setattr(self, prefix + attribute, event_dict[attribute])

        # Configure the child class
        self.configure()

        # Get list of suppressed parameters
        self.suppressed_params = self.suppressParametersInOutput()
        if self.suppressed_params is None:
            self.suppressed_params = []

        # Update the suppress output list

    def isDynamicObject(self, dynamic_object):
        try:
            # TODO: check pattern: $_(sensor_name)(dot)(object_name)
            if dynamic_object.startswith("$_") and len(dynamic_object) > 2:
                return True
        except:
            return False

    def registerDynamicObject(self, dynamic_object):
        try:
            object_name = dynamic_object[len("$_"):]
            first_dot = object_name.find(".")
            sensor_name = object_name[:first_dot]
            self.attached_sensors.add(sensor_name)
        except Exception as e:
            failEventConfiguration(self, "Error parsing dynamic object: " + str(dynamic_object) + "\n" + str(e))

    def getDynamicObject(self, dynamic_object):
        try:
            object_name = dynamic_object[len("$_"):]
            first_dot = object_name.find(".")
            sensor_name = object_name[:first_dot]
            attribute_name = object_name[first_dot + 1:]
            second_dot = attribute_name.find(".")
            if second_dot > -1:
                dict_element = attribute_name[second_dot + 1:]
                attribute_name = attribute_name[:second_dot]
                attribute = getattr(self.sensors_data[sensor_name], attribute_name)
                if attribute is not None:
                    return attribute[dict_element]
            return getattr(self.sensors_data[sensor_name], attribute_name)
        except Exception as e:
            failEventConfiguration(self, "Error parsing dynamic object: " + str(dynamic_object) + "\n" + str(e))
            return None

    @abstractmethod
    def configure(self):
        pass

    def getDict(self):
        # Return all the PARAM__ attributes except info and name
        prefix = "PARAM__"
        params = [i[len(prefix):] for i in self.__dict__ if i.startswith(prefix) and i not in [prefix + "info", prefix + "name"] and i not in self.suppressed_params]
        object_dict = {}
        for param in params:
            param_value = getattr(self, prefix + param)
            if self.isDynamicObject(param_value):
                param_value = self.getDynamicObject(param_value)
            object_dict[param] = param_value
        return object_dict

    @abstractmethod
    def listParameters(self):
        pass

    @abstractmethod
    def isTriggered(self):
        pass

    @abstractmethod
    def suppressParametersInOutput(self):
        pass
