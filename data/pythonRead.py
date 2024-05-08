from customtkinter.windows import CTk
from data.ThreadedFileReader import ThreadFileReader
import logging
import time
import random

class pythonRead (ThreadFileReader):
    def __init__(self, gui: CTk, Full_path: dict, logging: logging):
        super().__init__(gui, Full_path, logging)

    def process_logic(self, index):
        sleep=random.random()
        logging.debug(sleep)
        time.sleep(sleep)