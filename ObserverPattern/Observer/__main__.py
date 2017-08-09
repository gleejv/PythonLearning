from Observer.kpis import KPIs
from Observer.forecastkpi import ForecastKPIs
from Observer.currentkpi import CurrentKPIs

kpis=KPIs()
currentKPIs=CurrentKPIs(kpis)
forecastKPIs=ForecastKPIs(kpis)
kpis.set_kpis(25,10,5)
kpis.set_kpis(100,34,23)
kpis.set_kpis(23,60,46)

print("+++++++Detaching+++++++++++")
kpis.detach(currentKPIs)
kpis.set_kpis(232,454,98)