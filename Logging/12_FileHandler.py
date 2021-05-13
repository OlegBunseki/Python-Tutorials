import logging

# Create logger
logger = logging.getLogger(__name__) # the name can be hardcoded if I like
logger.setLevel(logging.DEBUG)       # DEFAULT: WARNING!

# Set file handler with formatter
file_handler = logging.FileHandler('Logging/logs/11_FileHandler.log')

# Set levels
file_handler.setLevel(logging.DEBUG)   # logger.setLevel is the treshold! Wont log DEBUG is logger is set to INFO!

# Create formatters
file_formatter = logging.Formatter('%(asctime)s: %(name)s: %(filename)s: %(levelname)s: %(message)s')

# Set fiel and stream handler with formatter
file_handler.setFormatter(file_formatter)

# Add Handler to Logger
logger.addHandler(file_handler)

# Log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

a = 20
b = 10

# logger.exception(msg, *args) is the same as calling logger.error(msg, *args, exc_info=True)

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

