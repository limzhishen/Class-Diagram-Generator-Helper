import logging
logging.basicConfig(format='Date-Time : %(asctime)s : - %(message)s', level = logging.DEBUG)
# log_file="app.log"
# file_handler = logging.FileHandler(log_file)
# logging.getLogger().addHandler(file_handler)
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(ColoredFormatter('Date-Time : %(asctime)s : - %(message)s'))
# logging.getLogger().addHandler(stream_handler)
# logging.getLogger().setLevel(logging.DEBUG)
class Changelogging():
    def __init__(self):
        self.logging=logging
    def debug_blue(self,messange):
        self.logging.debug(f'\033[94m{messange}\033[0m')
        # self.logging.debug(messange)
    def debug_yellow(self,messange):
        self.logging.debug(f'\033[93m{messange}\033[0m')
        # self.logging.debug(messange)
    def debug_red(self,messange):
        self.logging.debug(f'\033[91m{messange}\033[0m')
        # self.logging.debug(messange)
    def info_green(self,messange):
        self.logging.info(f'\033[92m{messange}\033[0m')
        # self.logging.info(messange)
    def critical_red(self,messange):
        self.logging.critical(f'\033[91m{messange}\033[0m')
        # self.logging.critical(messange)
