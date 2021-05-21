import logging
import logging.handlers
from functions import add_v2


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)         # TOP HIERACHY. IF NOT SET -> SET TO WARNING!

LOG_FILEPATH = 'Logging/logs/17_MultipleFileHandlers.log'

formatter = logging.Formatter('%(asctime)s: %(name)s: %(filename)s: %(levelname)s: %(message)s') 

file_handler = logging.FileHandler(LOG_FILEPATH)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
print(logger.handlers)

logger.addHandler(file_handler)
print(logger.handlers)

file_handler = logging.FileHandler(LOG_FILEPATH)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
print(logger.handlers)


# Log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

