from abc import ABC, abstractmethod

class BaseCompute(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def getPinMap(self):
        pass

    @abstractmethod
    def getPinLayout(self):
        pass
