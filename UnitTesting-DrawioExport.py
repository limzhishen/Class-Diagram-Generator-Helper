from export.drawio import drawio_export
from component.LoggingColorFormat import Changelogging
import time,customtkinter
from component.OutputComponent import OutputComponent


starttime=time.time()
abc=drawio_export(OutputComponent(customtkinter.CTk()),Changelogging(),max_worker=10,removefile=False)
abc.export()

endtime=time.time()
print(endtime-starttime)