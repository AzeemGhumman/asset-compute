from abc import ABC, abstractmethod

class BaseCompute(ABC):

    def __init__(self):
        super().__init__()

    def getPin(self, name):
        for pin in self.getPins():
            if pin.name == name:
                return pin
        return None

    @abstractmethod
    def getPins(self):
        pass

    @abstractmethod
    def getLayout(self):
        pass
