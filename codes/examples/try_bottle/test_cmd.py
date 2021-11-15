import time
import logging

logging.basicConfig(level=logging.DEBUG)

for i in range(1, 10):
    logging.debug("this is debug info {}".format(i))
    logging.error("this is error info {}".format(i))
    print("this is print info {}".format(i))
    time.sleep(1)
