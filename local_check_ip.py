import requests
import time

while True:
   try:
    session = requests.session()
    headers = {
    }
    proxies = {'http': 'http://10086:10086@192.168.31.135:35006',
               'https': 'http://10086:10086@192.168.31.135:35006'}
    url = "http://members.3322.org/dyndns/getip"
    r = requests.get(url=url, headers=headers, timeout=1,
                     proxies=proxies, verify=False)
    print(r.status_code, r.text, time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime()))
   except:
       pass
