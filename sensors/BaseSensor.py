#     configure(pass in generic object): one time
#     read(no parameters passed?): every time we want to read sensor data
#     parse(): convert raw data to something we can send to server

from abc import ABC, abstractmethod

class BaseSensor(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def configure(self, sensorConfiguration):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def clean(self):
        pass
