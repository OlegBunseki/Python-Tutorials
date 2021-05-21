import logging
import logging.config
import yaml
import logging.handlers
import json
from functions import add_v4


LOGPATH_YAML = 'Logging/logging.yaml'
LOGPATH_JSON = 'Logging/logging.json'
LOG_LEVEL = 'dev'

### YAML ###

with open(LOGPATH_YAML, 'rt') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(LOG_LEVEL)
print(logger.handlers)

# logger = logging.getLogger()
# print(logger.handlers)


### JSON ###

# with open(LOGPATH_JSON, 'rt') as f:
#   config = json.load(f)
#   logging.config.dictConfig(config)

# logger = logging.getLogger(LOG_LEVEL)
# print(logger.handlers)

# logger = logging.getLogger()
# print(logger.handlers)


### EMPTY ###

# logger = logging.getLogger()
# print(logger.handlers)


logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

print('calling add_v4...')
add_v4(2, 2, LOG_LEVEL)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')