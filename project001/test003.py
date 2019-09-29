#coding=utf-8
import logging
DATEFMT = "[%Y-%m-%d %H:%M:%S]"
FORMAT = "%(asctime)s %(thread)d %(message)s"
logging.basicConfig(level=logging.INFO,format=FORMAT,datefmt=DATEFMT,filename='class_test.log')
logger = logging.getLogger(__name__)

try:
    print 1/0
except Exception,e:
    logging.critical(e)

