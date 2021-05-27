import requests
import time

while True:
   try:
    session = requests.session()
    headers = {
    }
    proxies = {'http': 'http://10086:10086@aoba.vip:13014',
               'https': 'http://10086:10086@aoba.vip:13014'}
    url = "http://members.3322.org/dyndns/getip"
    r = requests.get(url=url, headers=headers, timeout=1,
                     proxies=proxies, verify=False)
    print(r.status_code, r.text, time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime()))
   except:
       pass
