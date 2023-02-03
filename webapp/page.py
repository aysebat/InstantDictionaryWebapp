from abc import ABC, abstractmethod


#inhereit from ABC
class Page(ABC):
    """This class is an abstract  class and method is an abstract method"""
    @abstractmethod
    def serve(self):
        pass