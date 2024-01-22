# build the logger
import logging
logging.basicConfig(level=logging.DEBUG, filename='loger.log', format='%(asctime)s - %(levelname)s - %(message)s')



class Logger:
    def __init__(self):
        self.logger = logging.getLogger('myLoger')

    def info(self, message):
        print(message)
        self.logger.info(message)

