import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    logger_formatter = logging.Formatter(
        "[%(asctime)s]{%(filename)s:%(lineno)d}-10s: %(levelname)s - %(message)s"
    )
    stream_handler.setFormatter(logger_formatter)
    logger.addHandler(stream_handler)
    return logger
