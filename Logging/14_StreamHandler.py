import logging
import sys

# Create logger
logger = logging.getLogger(__name__) # the name can be hardcoded if I like
logger.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s: %(name)s: %(filename)s: %(levelname)s: %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(file_formatter)

logger.addHandler(stream_handler)

# Log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

a = 20
b = 10

def devide(a, b):
    try:
        r = a/b
        logger.debug(f'result a/b: {r}')
        return r
    except Exception as e:
        logger.exception(f'result a/b: {e}')
        return None

def devide_v2(a, b):
    try:
        r = a/0
        logger.debug(f'result a/b: {r}')
        return r
    except Exception as e:
        logger.exception(f'result a/b: {e}')
        return None


logger.info('Calling devide function with arguments {} and {}'.format(a, b))
result = devide(a, b)

if result is not None:
    logger.info(result)
else:
    logger.info('Deviation failed')


logger.info('Calling second devide function with arguments {} and {}'.format(a, b))
result = devide_v2(a, b)

if result is not None:
    logger.info(result)
else:
    logger.warning('Deviation failed')