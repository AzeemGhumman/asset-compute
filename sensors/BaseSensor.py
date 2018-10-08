from abc import ABC, abstractmethod

'''
TODO:

Common tasks for each sensor
- set common data members
- check valid pins, data and event names

in configure() in each sensor
- test if each pin is connected to compatible type
.. if after writing a few sensors, we realize that the check pin logic
is common, we can move it to the parent sensor class
..also can create a helper routine in the base class to do the boiler plate
common matching on each pin..

.. also set pins, and other variables in configure

in read()
- update data elements and event names

in write()
- return a dictionary object with all the request information that's avaiable


'''

import sys

# Load common
sys.path.append('../scripts/helper/')
from common import fail, failSensorConfiguration, createClassLevelObjects, ComputePinTag

import pdb

class BaseSensor(ABC):

    def __init__(self):
        super().__init__()
        self.name = None
        self.signal_elements = []
        self.connections = []
        self.params = {}

    def __setPins(self):
        prefix = "PIN__"
        createClassLevelObjects(class_object = self, prefix = prefix, variable_list = self.listPins())
        known_pins = [i[len(prefix):] for i in [*vars(self)] if i.startswith(prefix)]
        for pin in self.connections:
            pin_name = pin.sensor_pin.name
            if pin_name not in known_pins:
                failSensorConfiguration ("Unknown sensor pin '" + pin_name + "' for sensor: " + self.name + "'")
            setattr(self, prefix + pin_name, pin.compute_pin)

    def __setSignals(self):
        createClassLevelObjects(class_object = self, prefix = "", variable_list = self.listSignals())
        prefix = "HAS_SIGNAL__"
        createClassLevelObjects(class_object = self, prefix = prefix, variable_list = self.listSignals())
        known_signals = [i[len(prefix):] for i in [*vars(self)] if i.startswith(prefix)]
        for signal in self.signal_elements:
            if signal not in known_signals:
                failSensorConfiguration ("Unknown signal '" + signal + "' for sensor: " + self.name + "'")
            setattr(self, prefix + signal, True)

    def __setParameters(self):
        prefix = "PARAM__"
        createClassLevelObjects(class_object = self, prefix = prefix, variable_list = self.listParameters())
        known_params = [i[len(prefix):] for i in [*vars(self)] if i.startswith(prefix)]
        for param in self.params:
            if param not in known_params:
                failSensorConfiguration ("Unknown param '" + param + "' for sensor: " + self.name + "'")
            setattr(self, prefix + param, self.params[param])

    def setSensorConfigurations(self, name, signal_elements, connections, params):
        self.name = name
        self.signal_elements = signal_elements
        self.connections = connections
        self.params = params

        # TODO:
        '''
        get all pins, data and event from class
        checks:
        - all pins must be present in connections
        - all data in signal_elements must be present in class
        - all evenets in ....

        set all pinNumbers in class to what is coming from connections
        # let the child class ask for compatibility tests based on tags

        # when write is called from main loop
        # we internally call the clean method of the child class?
        then, based on the signal_elements and event_elements requested,
        we generate the final dictionary object that is returned to
        the runner.

        TODO: Create 2 sensors as example,
        one with the bare minimum and other with interesting fucntionaluity events and params, etc.
        EVENT: humidity boundary crossed of 70 percent
        WENT_OVER_70, WENT_UNDER_70??
        DATA: convert temperature to farenheit
        Sensor-level param example: ? version, model, etc.
        e.g DHT11 or 12 having the same sensor file!


        When creating a dict object, only include a value if it is not None
        applies for both signals and events


        '''
        self.__setPins()
        self.__setSignals()
        self.__setParameters()

        self.configure()

    def writeData(self, events_data):

        self.beforeWrite()

        signals = {}
        # Add all the signals
        for signal in self.signal_elements:
            try:
                signal_value = getattr(self, signal)
                if signal_value is not None:
                    signals[signal] = signal_value
            except:
                fail("Sensor: '" + self.name + "' does not contain member: " + signal)

        # For all events linked with this signal, run isTriggered() and add to response
        events_triggered = {}
        for event in events_data:
            if self.name in event.attached_sensors:
                try:
                    if event.isTriggered():
                        events_triggered[event.PARAM__name] = event.getDict()
                except Exception as e:
                    print ("Error while running isTriggered() for event: " + str(event.PARAM__info) + "\n" + str(e))

        response = {}
        if len(signals) > 0:
            response['signals'] = signals
        if len(events_triggered) > 0:
            response['events'] = events_triggered

        self.afterWrite()
        return response

    @abstractmethod
    def listSignals(self):
        pass

    @abstractmethod
    def listParameters(self):
        pass

    @abstractmethod
    def listPins(self):
        pass

    @abstractmethod
    def configure(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def beforeWrite(self):
        pass

    @abstractmethod
    def afterWrite(self):
        pass
