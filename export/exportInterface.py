from abc import ABC,abstractmethod

class Export(ABC):
    @abstractmethod
    def export(self,index):
        pass