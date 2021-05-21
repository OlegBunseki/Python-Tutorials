import logging

# INFO: https://docs.python.org/3/library/logging.html
# INFO: https://docs.python.org/3/howto/logging.html


# https://www.youtube.com/watch?v=-ARI4Cz-awo

# https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

# By default, there are 5 standard levels indicating the severity of events. 
# Each has a corresponding method that can be used to log events at that level of severity. 
# The defined levels, in order of increasing severity, are the following:

# 1. DEBUG    - 10
# 2. INFO     - 20
# 3. WARNING  - 30
# 4. ERROR    - 40
# 5. CRITICAL - 50

logging.info('Hello')
logging.debug('Hello')
logging.warning('Hello')
logging.error('Hello')
logging.critical('Hello')