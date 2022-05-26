#encoding=utf-8

import logging
import logging.handlers
import sys
import io
import time

# filename filemode format datefmt level stream
logging.basicConfig(
	#filename="root.txt", filemode="a", 
	level=logging.DEBUG,
	format="%(asctime)s  %(name)s  %(levelname)s %(message)s [[%(pathname)s:%(funcName)s:%(lineno)d]]",
	datefmt="%Y-%m-%d %H:%M:%S",
	stream=sys.stdout
	)

formater = logging.Formatter(
	fmt="%(asctime)s  %(name)s  %(levelname)s %(message)s [[%(pathname)s:%(funcName)s:%(lineno)d]]",
	datefmt="%Y-%m-%d %H:%M:%S")


streamStream = io.open("stream_logger.txt", "w", buffering=-1, encoding="utf-8")
streamHandler = logging.StreamHandler(streamStream)
streamHandler.setFormatter(formater)
streamHandler.setLevel(logging.INFO)
streamLogger = logging.getLogger("streamLogger")
streamLogger.addHandler(streamHandler)

fileHandler = logging.FileHandler("file_logger.txt", "w", encoding="utf-8", delay=True)
fileHandler.setFormatter(formater)
fileHandler.setLevel(logging.INFO)
fileLogger = logging.getLogger("fileLogger")
fileLogger.addHandler(fileHandler)

nullLogger = logging.getLogger("nullHandler")
nullLogger.addHandler(logging.NullHandler())

rotatingFileHandler = logging.handlers.RotatingFileHandler( 
	filename="rotating_file_logger.txt", mode="a", 
	maxBytes=100, backupCount=1, 
	encoding="utf-8", delay=True)
rotatingFileHandler.setFormatter(formater)
rotatingFileHandler.setLevel(logging.INFO)
rotatingFileLogger = logging.getLogger("rotatingFileLogger")
rotatingFileLogger.addHandler(rotatingFileHandler)

timeRotatingFileHandler = logging.handlers.TimedRotatingFileHandler(
		filename="time_rotating_file_logger.txt",
		when="S", interval=10, backupCount=-1,
		encoding="utf-8", delay=True, utc=False)
timeRotatingFileHandler.setFormatter(formater)
timeRotatingFileHandler.setLevel(logging.INFO)
timeRotatingFileLogger = logging.getLogger("timeRotatingFileLogger")
timeRotatingFileLogger.addHandler(timeRotatingFileHandler)


#logFilter = logging.Filter(name="streamLogger")

logging.debug("test logging debug")
logging.info("test logging info")

streamLogger.debug(u"test streamLogger debug")
streamLogger.info(u"test streamLogger info 你好啊")

fileLogger.debug("test fileLogger debug")
fileLogger.info("test fileLogger info")

nullLogger.debug("test fileLogger debug")
nullLogger.info("test fileLogger info")

rotatingFileLogger.debug("test rotatingFileLogger debug")
rotatingFileLogger.info("test rotatingFileLogger 1 info")
rotatingFileLogger.info("test rotatingFileLogger 2 info")

timeRotatingFileLogger.debug("test timeRotatingFileLogger debug")
timeRotatingFileLogger.info("test timeRotatingFileLogger info 1")

#time.sleep(11)
#timeRotatingFileLogger.info("test timeRotatingFileLogger info 2")

adapterFormater = logging.Formatter(
	fmt="%(asctime)s  %(name)s  %(levelname)s [adapter:%(host)s:%(port)s] %(message)s ",
	datefmt="%Y-%m-%d %H:%M:%S")

adapterHandler = logging.StreamHandler()
adapterHandler.setFormatter(adapterFormater)
adapterHandler.setLevel(logging.DEBUG)
adapterLogger = logging.getLogger("adapterLogger")
adapterLogger.addHandler(adapterHandler)

adapterDict = {"host":"www.luoxiaolong.com", "port":"80"}
loggerAdapter = logging.LoggerAdapter(adapterLogger, adapterDict)
loggerAdapter.debug("test loggerAdapter debug")
loggerAdapter.info("test loggerAdapter info")

class CustomAdapterLogger(logging.LoggerAdapter):
	def process(self, msg, kwargs):
		newMsg = msg + " [adapter {0[host]}:{0[port]} ]".format(self.extra)
		return (newMsg, kwargs)

customAdapterLogger = CustomAdapterLogger(
	logging.getLogger("customAdapterLogger"), adapterDict)

customAdapterLogger.debug("1234")













