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


class BaseSensor(ABC):

    def __init__(self):
        super().__init__()
        self.name = None
        self.dataElements = []
        self.eventElements = []
        self.connections = []

    def setSensorConfigurations(self, name, dataElements, eventElements, connections):
        self.name = name
        self.dataElements = dataElements
        self.eventElements = eventElements
        self.connections = connections

    @abstractmethod
    def configure(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass
