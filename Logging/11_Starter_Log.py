import logging
import logging.config

# With the logging module imported, you can use something called a “logger” to log messages that you want to see. 

# You can use the basicConfig(**kwargs) method to configure the logging.

### !!!NOTE!!! ###
# Loggers should NEVER be instantiated directly, but always through the module-level function logging.getLogger(name). 
# Multiple calls to getLogger() with the same name will always return a reference to the same Logger object.
# This however still works:


logging.basicConfig() 

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


### logging.basicConfig() ### 
# The basic configuration for the logging system creates a StreamHandler with a default Formatter and adds it to the root logger. 
# The functions debug(), info(), warning(), error() and critical() will call basicConfig() automatically if no handlers are defined for the root logger.


logging.basicConfig() 
logger = logging.getLogger(__name__)

# Run Log - First try
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')


### logging.basicConfig() WITH Paramters won't work as it is already set ### 

# This function does NOTHING if the root logger already has handlers configured, unless the keyword argument force is set to True.
# Create a Logging File (this will be filled up with every new message)

# Some of the commonly used parameters for basicConfig() are the following:

# 1. level: The root logger will be set to the specified severity level.
# 2. filename: This specifies the file.
# 3. filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
# 4. format: This is the format of the log message.


# By using the level parameter, you can set what level of log messages you want to record. 
# This can be done by passing one of the constants available in the class, 
# and this would enable all logging calls at or above that level to be logged.

logging.basicConfig(filename='./Logging/logs/11_Starter_Log.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s: %(filename)s: %(levelname)s: %(message)s'
                    )

# filename - Specifies that a FileHandler be created, using the specified filename, rather than a StreamHandler.

logger = logging.getLogger(__name__)

# Run Log - First try
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')



