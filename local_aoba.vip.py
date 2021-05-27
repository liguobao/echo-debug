import requests
import time
from loguru import logger

while True:
    try:
        session = requests.session()
        headers = {}
        proxies = {'http': 'http://10086:10086@aoba.vip:13016',
                   'https': 'http://10086:10086@aoba.vip:13016'}
        url = "http://house-map.cn"
        r = requests.get(url=url, headers=headers, timeout=1,
                         proxies=proxies, verify=False)
        logger.info(f"status_code:{r.status_code},auto sleep 1s")
        time.sleep(1)
    except Exception as err:
        print(f"requests fail,error:{str(err)},auto sleep 1s")
        time.sleep(1)
