import logging
from config_helper.config import get_prefix, get_config_params


def log_config(module: str = "generic"):
    """
    Configures the logger for the application & returns it.
    :param module: Name that will prefix every message
    :return: The logger
    """
    prefix = get_prefix()
    config = get_config_params()
    log_level = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARN': logging.WARN,
        'ERROR': logging.ERROR,
    }
    logger = logging.getLogger(f'{prefix}-{module}')
    logging.basicConfig()
    log_level_option = config["log_level"]
    try:
        logger.setLevel(log_level[log_level_option])
    except:
        logger.setLevel(log_level["WARN"])
    return logger