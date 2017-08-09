from abc import ABCMeta,abstractmethod
from Observer.observer.observer_abc import Abs_Observer

class Abs_Subject(object,metaclass=ABCMeta):
    _observers=set()

    def attach(self,observer):
        if not isinstance(observer,Abs_Observer):
            raise TypeError('Observer not derived from Abs_Observer')
        self._observers |= {observer}

    def detach(self,observer):
        self._observers-={observer}

    def notify(self,value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

