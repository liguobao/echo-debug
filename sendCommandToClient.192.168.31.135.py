from logging import log
import requests
from loguru import logger
from urllib.parse import quote
import time

echo_host = "http://192.168.31.135"


def user_login():
    url = f"{echo_host}:8998/echo-api/user-info/login"
    payload = 'userName=admin&password=admin'
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'token': 'undefined',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'EN',
        'x_identify_user': 'test'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()["data"]["loginToken"]


def refresh_token(login_token):
    url = url = f"{echo_host}:8998/echo-api/user-info/refreshToken"
    payload = {}
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'token': login_token,
        'Accept-Language': 'EN',
        'x_identify_user': 'test'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        logger.error(f"refresh_token fail,response:{response.text}")
        return None


def send_command_to_client(client_id, refresh_token, action="ShizukuReDial"):
    url = url = f"{echo_host}:4826/echo-api/nat-mapping-server/sendCommandToClient?clientId={quote(client_id)}&action={action}&additionParam=whoami&token={refresh_token}"
    response = requests.request("GET", url, headers={})
    logger.info(
        f"{action} finish,client_id:{client_id},response:{response.text}")


def get_connection_list():
    url = f"{echo_host}:4826/echoNatApi/connectionList?serverId=echo-http-proxy-001"
    response = requests.request("GET", url, headers={})
    if response.status_code == 200:
        return response.json()["clients"]
    else:
        logger.error(f"get_connection_list fail,response:{response.text}")
        return []


def get_proxy_resources():
    url = f"http://192.168.31.135:8998/echo-api/proxy-resource/query?Token=435780e8-6589-4afe-a32f-c3506ae96d1f&size=10&random=false&detail=true"
    response = requests.request("GET", url, headers={})
    if response.status_code == 200:
        return response.json()["data"]
    else:
        logger.error(f"get_connection_list fail,response:{response.text}")
        return []


def check_client_id(client_id, check_count=5):
    for index in range(0, check_count):
        connection_list = get_connection_list()
        connection_clients = [x["clientId"] for x in connection_list]
        if client_id in connection_clients:
            logger.info(f"connection_client:{client_id} online ready")
        else:
            logger.warning(
                f"connection_client:{client_id} offline successfully.")
        proxy_resources = get_proxy_resources()
        proxy_clients = [x["clientId"] for x in proxy_resources]
        if client_id in proxy_clients:
            proxy_resource = [
                x for x in proxy_resources if x["clientId"] == client_id][0]
            proxy_info = f"{proxy_resource['proxyIp']}:{proxy_resource['proxyPort']}"
            logger.info(
                f"proxy_client:{client_id} online ready,proxy_info:{proxy_info}")
            check_proxy_resource(proxy_info)
        else:
            logger.warning(f"proxy_client:{client_id} offline successfully.")
        time.sleep(1)
        logger.info(f"check_client_id finish,index:{index},sleep 1s finished")


def check_proxy_resource(proxy):
    try:
        session = requests.session()
        headers = {}
        proxies = {'http': f'http://10086:10086@{proxy}',
                   'https': 'http://10086:10086@{proxy}'}
        url = "http://www.baidu.com"
        r = requests.get(url=url, headers=headers, timeout=3,
                         proxies=proxies, verify=False)
        logger.info(f"check_proxy finish,status_code:{r.status_code}")
    except Exception as err:
        print(f"check_proxy fail,error:{str(err)}")


client_id = "admin|@--@--@|353626072983559_9262"
login_token = user_login()


def sleep_seconds(second):
    logger.info(f"sleep {second}s start")
    for i in range(0, second):
        logger.info(f"sleep {i+1}s ...")
        time.sleep(1)


while True:
    admin_token = refresh_token(login_token)
    if not admin_token:
        logger.info("sleep 2s")
        time.sleep(2)
        continue
    send_command_to_client(client_id, admin_token)
    check_client_id(client_id, 30)
    sleep_seconds(20)
