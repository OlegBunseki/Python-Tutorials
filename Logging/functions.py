import numpy as np
import logging

def add(a, b):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) 

    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler('Logging/logs/14_Modeules_fh2.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    logger.debug('Inside Call Function')
    logger.info('Inside Call Function')
    logger.warning('Inside Call Function')
    logger.error('Inside Call Function')
    logger.critical('Inside Call Function')
    
    result = np.int(a) + np.int(b)
    return result
