import logging
from functions import add

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s: %(name)s: %(filename)s: %(levelname)s: %(message)s')


fh1 = logging.FileHandler('Logging/logs/15_Modeules_fh1.log')
fh1.setLevel(logging.DEBUG)
fh1.setFormatter(file_formatter)
logger.addHandler(fh1)


fh2 = logging.FileHandler('Logging/logs/15_Modeules_fh2.log')
fh2.setLevel(logging.WARNING)
fh2.setFormatter(file_formatter)
logger.addHandler(fh2)


logger.debug('Inside Main Function')
logger.info('Inside Main Function')
logger.warning('Inside Main Function')
logger.error('Inside Main Function')
logger.critical('Inside Main Function')


logger.info('Calling Function ADD')
logger.warning('a and b will be converted to int inside the function')
r = add(2, 2)
logger.info(f'Result is {r}')

