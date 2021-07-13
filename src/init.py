import datetime
import logging


def init_logging(dt_now: datetime, mode: str):
    filename = _logging_file_name(dt_now=dt_now)
    level = logging.DEBUG if (mode == 'debug') else logging.INFO
    log_format = '[%(levelname)s] %(asctime)s %(message)s'

    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    formatter = logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S')

    handler = logging.FileHandler(filename)
    handler.setFormatter(formatter)
    handler.setLevel(level)
    logger.addHandler(handler)

    handler2 = logging.StreamHandler()
    handler2.setFormatter(formatter)
    handler2.setLevel(level)
    logger.addHandler(handler2)

    logger.propagate = False
    return logger


def _logging_file_name(dt_now: datetime) -> str:
    return f"./storage/logs/{format(dt_now, '%Y-%m-%d')}_python.log"
