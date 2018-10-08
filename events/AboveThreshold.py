#!/usr/bin/python

from BaseEvent import BaseEvent
import pdb
import sys
sys.path.append('../scripts/helper/')
from common import fail, failEventConfiguration

class AboveThreshold(BaseEvent):
    def __init__(self):
        super().__init__()

    def listParameters(self):
        return ["signal_name", "signal_value", "threshold"]

    def configure(self):
        if self.PARAM__signal_name is None:
            failEventConfiguration(self, "signal_name is missing")

        if self.PARAM__signal_value is None:
            failEventConfiguration(self, "signal_value is missing")

        if self.PARAM__threshold is None:
            failEventConfiguration(self, "threshold is missing")

        # Register dynamic resources
        self.registerDynamicResource(self.PARAM__signal_value)

    def isTriggered(self):

        signal_value = self.getDynamicObject(self.PARAM__signal_value)
        if signal_value is not None and int(signal_value) > self.PARAM__threshold:
            return True
        return False

    def suppressParametersInOutput(self):
        pass
