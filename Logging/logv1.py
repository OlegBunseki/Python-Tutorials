import logging
# import logv2 # During import the entire script is run. All logs are logged.
from logv2 import devide, devide_v2

# Create logger
logger = logging.getLogger(__name__) # the name can be hardcoded if I like
logger.setLevel(logging.DEBUG)

# Set file handler with formatter
file_handler = logging.FileHandler('logv1.log')
stream_handler = logging.StreamHandler()

# Set levels
file_handler.setLevel(logging.INFO)
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
logger.debug('This is a debug message v1')
logger.info('This is an info message v1')
logger.warning('This is a warning message v1')
logger.error('This is an error message v1')
logger.critical('This is a critical message v1')

a = 20
b = 0

logger.info('Calling devide function with arguments {} and {}'.format(a, b))
devide(a, b)

logger.info('Calling second devide function with arguments {} and {}'.format(a, b))
devide_v2(a, b)

