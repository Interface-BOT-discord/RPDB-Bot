import sys

from loguru import logger

logger.remove()
logger.add('logs/logs/log.log',
           level="DEBUG",
           rotation="10 KB",
           compression="zip",
           format="{time} - {level}: {message}")
logger.add(sys.stderr, level="WARNING", format="{level} | {message}")


def debug(msg):
    logger.debug(msg)


def info(msg):
    logger.info(msg)


def warn(msg):
    logger.warning(msg)


def error(msg):
    logger.error(msg)


def critical(msg):
    logger.critical(msg)
