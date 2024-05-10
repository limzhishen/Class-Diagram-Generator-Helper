import logging
logging.basicConfig(format='Date-Time : %(asctime)s : - %(message)s', level = logging.DEBUG)

class Changelogging():
    def __init__(self):
        self.logging=logging
    def debug_blue(self,messange):
        self.logging.debug(f'\033[94m{messange}\033[0m')
    def debug_red(self,messange):
        self.logging.debug(f'\033[91m{messange}\033[0m')
    def info_green(self,messange):
        self.logging.info(f'\033[92m{messange}\033[0m')

abc=Changelogging()
abc.debug_blue("gogogd")
abc.debug_red("redredered")
abc.info_green("sdadasdasdsa")