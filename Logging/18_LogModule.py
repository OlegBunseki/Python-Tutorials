from utils_logger import get_logger
print('START')
logger = get_logger(logger_name='main.app')   # otherwise it will be always utils_logger.py
print(__name__, logger.handlers)

from functions import add_v3
import logging


# Log messages
print('logging messages...')
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

print('calling add_v3...')
add_v3(2, 2)


logger = get_logger(logger_name='main.app')
print(__name__, logger.handlers)

print('logging messages again...')
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
