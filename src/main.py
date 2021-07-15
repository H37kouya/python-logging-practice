import lib
from app.log import logger


def main() -> None:
    lib.lib_hello(logger)
    print("Hello World")


if __name__ == "__main__":
    logger.info("System Start")
    main()
    logger.info("System End")
