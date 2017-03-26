import logging
import sys

logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler(sys.stdout)
stream_formatter = logging.Formatter('%(name)s : %(asctime)s %(levelname)s(%(levelno)s) %(filename)s:%(lineno)s %(module)s:%(funcName)s:%(lineno)s - %(message)s')
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)

file_handler = logging.FileHandler("logfile.txt")
file_formatter = logging.Formatter('%(name)s : %(asctime)s %(levelname)s(%(levelno)s) %(filename)s:%(lineno)s %(module)s:%(funcName)s:%(lineno)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.debug("Print Log Not In Function !")

def DoLogInFunction(logger):
	logger.debug("Print Log In Function !")

DoLogInFunction(logger)





