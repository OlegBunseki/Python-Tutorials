import numpy as np
import logging
from utils_logger import get_logger


def add(a, b):

    logger = logging.getLogger(__name__)
    
    logger.setLevel(logging.DEBUG) 

    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler('Logging/logs/15_Modeules_fh2.log')
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    logger.debug('Inside Call Function - DEBUG')
    logger.info('Inside Call Function - INFO')
    logger.warning('Inside Call Function - WARNING')
    logger.error('Inside Call Function - ERROR')
    logger.critical('Inside Call Function - CRITICAL')
    
    result = np.int(a) + np.int(b)
    return result

def add_v2(a, b):

    logger = logging.getLogger(__name__)   
    logger.setLevel(logging.DEBUG) 

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.ERROR)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    logger.debug('Inside Call Function - DEBUG')
    logger.info('Inside Call Function - INFO')
    logger.warning('Inside Call Function - WARNING')
    logger.error('Inside Call Function - ERROR')
    logger.critical('Inside Call Function - CRITICAL')
    
    result = np.int(a) + np.int(b)
    return result


def add_v3(a, b):

    logger = get_logger(logger_name='add.app')

    print('add_v3', logger.handlers)

    logger.debug('Inside Call Function')
    logger.info('Inside Call Function')
    logger.warning('Inside Call Function')
    logger.error('Inside Call Function')
    logger.critical('Inside Call Function')
    
    result = np.int(a) + np.int(b)
    return result


def add_v4(a, b, log_level):

    logger = logging.getLogger(log_level)

    print('add_v4', logger.handlers)

    logger.debug('Inside Call Function')
    logger.info('Inside Call Function')
    logger.warning('Inside Call Function')
    logger.error('Inside Call Function')
    logger.critical('Inside Call Function')
    
    result = np.int(a) + np.int(b)
    return result