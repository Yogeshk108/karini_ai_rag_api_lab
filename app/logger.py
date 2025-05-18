import logging

LOG_LEVEL = 'INFO'

LOG_FORMAT = (
    "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
)


def configure_root_logger():
    """
    Configures the root logger with the specified log level and format.
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)

    if not root_logger.hasHandlers():
        handler = logging.StreamHandler()
        handler.setLevel(LOG_LEVEL)
        handler.setFormatter(logging.Formatter(LOG_FORMAT))
        root_logger.addHandler(handler)


def get_logger(logger_name: str) -> logging.Logger:
    """
    Returns a logger with the specified name and log level.
    :param logger_name: name of module in which logger initialized
    :return: logger object
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(LOG_LEVEL)

    return logger


configure_root_logger()
