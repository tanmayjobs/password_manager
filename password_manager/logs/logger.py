"""
This file create a Logger class used to log anything in the system.
This file also setups the basic logging system.
"""

import logging
from logging import INFO, DEBUG, WARN, CRITICAL, ERROR

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/server.log",
    filemode="a+",
    format="%(asctime)s %(levelname)-10s %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
)


class Logger:

    @staticmethod
    def log(lvl: int, msg: str, specific_name="server"):
        spc_logger = logging.getLogger(specific_name)
        spc_logger.log(lvl, msg)
