import logging
import logging.handlers

# Set up logger with appropriate handler
LOG_FILEPATH = 'Logging/logs/13_RotatingFileHandler'

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(LOG_FILEPATH, maxBytes=1000, backupCount=5)

logger.addHandler(handler)

# Rolling over to simulate log exceeding maxBytes size
# handler.doRollover()

for i in range(1000):
    logger.info(f'This is iteration number: {i}')    
