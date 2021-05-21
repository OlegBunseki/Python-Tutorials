import logging

def get_logger(logger_name= __name__, log_base_level=logging.DEBUG, fh_name='Logging/logs/sys.log', fh_log_level=logging.DEBUG):

    logger = logging.getLogger(logger_name)
    print('F1, logger_name', logger_name, logger.handlers)

    logger.setLevel(log_base_level)

    formatter = logging.Formatter('%(asctime)s: %(name)s: %(filename)s: %(levelname)s: %(message)s') 

    file_handler = logging.FileHandler(fh_name)
    file_handler.setLevel(fh_log_level)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    print('F2, logger_name', logger_name, logger.handlers)

    return logger


