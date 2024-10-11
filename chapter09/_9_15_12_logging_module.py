import logging

logger = logging.getLogger(__name__)


# Function that uses logging.
def func():
    logger.debug("A debugging message.")
    logger.info("An informational message.")
    logger.warning("A warning message.")
    logger.error("An error message.")
    logger.critical("A critical message.")


# Configuration of logging (occurs once at program startup)
if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING, filename="9_15_12_output.log")
    func()
