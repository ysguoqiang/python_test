import logging

logger = logging.getLogger(__name__)
logging.root.setLevel(logging.DEBUG)
logFormat = logging.Formatter('%(asctime)s %(filename)s:%(lineno)s %(funcName)s %(levelname)s %(message)s')

streamLog = logging.StreamHandler()
streamLog.setLevel(logging.INFO)
streamLog.setFormatter(logFormat)
logger.addHandler(streamLog)

fileLog = logging.FileHandler('get.log', mode='w', encoding='utf-8')
fileLog.setLevel(logging.ERROR)
fileLog.setFormatter(logFormat)
logger.addHandler(fileLog)