from Observer.observer.observer_abc import Abs_Observer

class ForecastKPIs(Abs_Observer):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self,kpis):
        self._kpis=kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets=self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print("Forecast open tickets: {}".format(self.open_tickets))
        print("forecast new tickets: {}".format(self.new_tickets))
        print("Forecast closed tickets: {}".format(self.closed_tickets))
        print("*******\n")