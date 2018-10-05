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

import pdb

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

        # TODO:
        '''
        get all pins, data and event from class
        checks:
        - all pins must be present in connections
        - all data in dataElements must be present in class
        - all evenets in ....

        set all pinNumbers in class to what is coming from connections
        # let the child class ask for compatibility tests based on tags

        # when write is called from main loop
        # we internally call the clean method of the child class?
        then, based on the dataelements and eventelements requested,
        we generate the final dictionary object that is returned to
        the runner.

        # TODO: separate method for each event? maybe update all
        # events for now in the read() and clean() and put only
        # the requested objects in the final dict

        keep all events in one function for now

        ! instead of write or clean
        add a pre-write and post-write hook
        the runner should call both hooks

        ! Aha
        add PARAM__EVENT__paramName
        change the manifest to let event take parameters
        let data take params and let the sensor take params
        PARAM__DATA__paramName
        PARAM_SENSOR_paramName


        '''
        pdb.set_trace()

    @abstractmethod
    def configure(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def clean(self):
        pass
