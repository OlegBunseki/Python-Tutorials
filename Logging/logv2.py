import logging

# Create logger
logger = logging.getLogger(__name__) # the name can be hardcoded if I like
logger.setLevel(logging.DEBUG)

# Set file handler with formatter
file_handler = logging.FileHandler('logv1.log')
stream_handler = logging.StreamHandler()

# Set levels
file_handler.setLevel(logging.DEBUG)
stream_handler.setLevel(logging.INFO)

# Create formatters
file_formatter = logging.Formatter('%(asctime)s: %(name)s: %(filename)s: %(levelname)s: %(message)s')
stream_formatter = logging.Formatter('Stream: %(asctime)s: %(name)s: %(filename)s: %(levelname)s: %(message)s')

# Set fiel and stream handler with formatter
file_handler.setFormatter(file_formatter)
stream_handler.setFormatter(stream_formatter)

# Add Handler to Logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# Log messages
logger.debug('This is a debug message v2')
logger.info('This is an info message v2')
logger.warning('This is a warning message v2')
logger.error('This is an error message v2')
logger.critical('This is a critical message v2')

def multiply(x, y):
    return x*y

def devide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        # logger.error('Devided by zero')                  # Without traceback
        # logger.error('Devided by zero', exc_info=True)   # Works as logger.exception() as traceback
        logger.exception('Devided by zero')              # With traceback


def devide_v2(x, y):
    try:
        return int('a')
    except Exception as e:
        # logger.error(e)      # Without traceback, bit Error statement
        logger.exception(e)    # With traceback, bit Error statement