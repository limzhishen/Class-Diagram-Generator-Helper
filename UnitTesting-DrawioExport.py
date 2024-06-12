from export.drawio import drawio_export
from component.LoggingColorFormat import Changelogging
import time


starttime=time.time()
abc=drawio_export(Changelogging(),max_woker=10,removefile=False)
abc.export()

endtime=time.time()
print(endtime-starttime)