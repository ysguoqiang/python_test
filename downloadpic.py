import threading
import requests
import logger
import os
import re
import proxy  

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