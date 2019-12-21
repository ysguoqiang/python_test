import threading
import requests
import logging
import os
import re

logger = logging.getLogger(__name__)
logging.root.setLevel(logging.DEBUG)
logFormat = logging.Formatter('%(asctime)s %(filename)s:%(lineno)s %(funcName)s %(levelname)s %(message)s')

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
sh.setFormatter(logFormat)
logger.addHandler(sh)

# th = handlers.TimedRotatingFileHandler(filename='new.log',when='D',backupCount=3,encoding='utf-8')
fh = logging.FileHandler('get.log', mode='w', encoding='utf-8')
fh.setLevel(logging.ERROR)
fh.setFormatter(logFormat)
logger.addHandler(fh)

proxies = {
  "http": "http://127.0.0.1:1080",
  "https": "http://127.0.0.1:1080",
}

def download_file(url, path, dst_name):
    try:
        imgres = requests.get(url, proxies=proxies)
    except Exception as e:
        logger.error(e)
        logger.error(url)
    else:
        filename = path+'/'+dst_name
        if not os.path.exists(filename):
            with open(filename, "wb") as f:
                f.write(imgres.content)
                f.close()
                logger.info(dst_name + " download success")
        else:
            pass
            logger.info(dst_name + " already exist")
    finally:
        pass


def get_dst_filename():
    pass

if __name__ == "__main__":
    pass