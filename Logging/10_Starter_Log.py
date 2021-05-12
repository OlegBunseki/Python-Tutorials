import logging


# INFO: https://docs.python.org/3/library/logging.html

# With the logging module imported, you can use something called a “logger” to log messages that you want to see. 
# By default, there are 5 standard levels indicating the severity of events. 
# Each has a corresponding method that can be used to log events at that level of severity. 
# The defined levels, in order of increasing severity, are the following:

# 1. DEBUG
# 2. INFO
# 3. WARNING
# 4. ERROR
# 5. CRITICAL

# You can use the basicConfig(**kwargs) method to configure the logging.

# Some of the commonly used parameters for basicConfig() are the following:

# 1. level: The root logger will be set to the specified severity level.
# 2. filename: This specifies the file.
# 3. filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
# 4. format: This is the format of the log message.

# By using the level parameter, you can set what level of log messages you want to record. 
# This can be done by passing one of the constants available in the class, 
# and this would enable all logging calls at or above that level to be logged. Here’s an example:


# Create a Logging File (this will be filled up with every new message)
logging.basicConfig(filename='./Logging/logs/10_Starter_Log.log', 
                    level=logging.ERROR,
                    format='%(asctime)s: %(filename)s: %(levelname)s: %(message)s') 

# Run Log - First try
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')














