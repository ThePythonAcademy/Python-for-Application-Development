import logging

log_format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="my_application_log.log", level=logging.DEBUG, format=log_format)
logger = logging.getLogger()

logger.debug("This is a harmless message")
logger.info("Just some useful information")
logger.warning("I'm sorry, but you can't do that, Dave")
logger.error("You can't divide by 0!!!")
logger.critical("The whole internet is down")
