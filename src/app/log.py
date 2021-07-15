import datetime
import logging
import sys


class Singleton(object):
    """
    シングルトン
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "__instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class Log(Singleton):
    """
    ログのクラス
    """

    LOG_FORMAT = '[%(levelname)s] %(asctime)s %(message)s'

    def __init__(self, dt_now: datetime, mode: str):
        self.input = input
        self.dt_now = dt_now
        self.mode = mode
        self.logger = None
        self.generate_logger_instance()

    def generate_logger_instance(self):
        filename = self._logging_file_name(dt_now=self.dt_now)
        level = logging.DEBUG if (self.mode == 'debug') else logging.INFO
        log_format = self.LOG_FORMAT

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
        self.logger = logger
        print("abc", self.logger)
        return self.logger

    def _logging_file_name(self, dt_now: datetime) -> str:
        return f"./storage/logs/{format(dt_now, '%Y-%m-%d')}_python.log"


logger = Log(
    dt_now=datetime.datetime.now(),
    mode=sys.argv[1]
).logger
