import datetime
import logging
import sys
import init
import lib


def main(logger) -> None:
    lib.lib_hello(logger)
    print("Hello World")


if __name__ == "__main__":
    dt_now = datetime.datetime.now()
    # MODE
    mode = sys.argv[1]
    logger = init.init_logging(dt_now=dt_now, mode=mode)

    logger.info("System Start")
    main(logger)
    logger.info("System End")
