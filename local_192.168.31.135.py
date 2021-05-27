import requests
import time
from loguru import logger

while True:
    try:
        session = requests.session()
        headers = {}
        proxies = {'http': 'http://10086:10086@192.168.31.135:35005',
                   'https': 'http://10086:10086@192.168.31.135:35005'}
        url = "http://www.baidu.com"
        r = requests.get(url=url, headers=headers, timeout=1,
                         proxies=proxies, verify=False)
        logger.info(f"status_code:{r.status_code},auto sleep 1s")
        time.sleep(1)
    except Exception as err:
        print(f"requests fail,error:{str(err)},auto sleep 1s")
        time.sleep(1)
