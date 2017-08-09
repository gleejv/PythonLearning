from abc import ABCMeta,abstractmethod

class Abs_Observer(object,metaclass=ABCMeta):
    @abstractmethod
    def update(self,value):
        pass