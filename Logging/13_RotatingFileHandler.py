import logging
import logging.handlers

# Set up logger with appropriate handler
LOG_FILEPATH = 'Logging/logs/13_RotatingFileHandler'

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.RotatingFileHandler(LOG_FILEPATH, maxBytes=1000, backupCount=5)

file_formatter = logging.Formatter('%(asctime)s: %(name)s: %(filename)s: %(levelname)s: %(message)s')

rf_handler.setFormatter(file_formatter)

logger.addHandler(rf_handler)

# Rolling over to simulate log exceeding maxBytes size
# handler.doRollover()

for i in range(1000):
    logger.info(f'This is iteration number: {i}')    
